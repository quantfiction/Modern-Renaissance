from logging.config import ConvertingList, ConvertingDict, valid_ident
from logging.handlers import QueueHandler, QueueListener
import logging
from queue import Queue
import atexit
from discord_webhook import DiscordWebhook, DiscordEmbed

from modern_renaissance.utils import get_settings

settings = get_settings()


def _resolve_handlers(handler_list):
    if not isinstance(handler_list, ConvertingList):
        return handler_list

    # Indexing the list performs the evaluation.
    return [handler_list[i] for i in range(len(handler_list))]


def _resolve_queue(q):
    if not isinstance(q, ConvertingDict):
        return q
    if "__resolved_value__" in q:
        return q["__resolved_value__"]

    cname = q.pop("class")
    klass = q.configurator.resolve(cname)
    props = q.pop(".", None)
    kwargs = {k: q[k] for k in q if valid_ident(k)}
    result = klass(**kwargs)
    if props:
        for name, value in props.items():
            setattr(result, name, value)

    q["__resolved_value__"] = result
    return result


class QueueListenerHandler(QueueHandler):
    def __init__(
        self, handlers, respect_handler_level=False, auto_run=True, queue=Queue(-1)
    ):
        queue = _resolve_queue(queue)
        super().__init__(queue)
        handlers = _resolve_handlers(handlers)
        self._listener = QueueListener(
            self.queue, *handlers, respect_handler_level=respect_handler_level
        )
        if auto_run:
            self.start()
            atexit.register(self.stop)

    def start(self):
        self._listener.start()

    def stop(self):
        self._listener.stop()

    def emit(self, record):
        return super().emit(record)


class DiscordHandler(logging.Handler):
    """
    Custom handler to send certain logs to Discord
    """

    def __init__(self):
        logging.Handler.__init__(self)
        self.discordWebhook = DiscordWebhook(url=settings["urls"]["discord"]["log"])

    def emit(self, record):
        """
        sends a message to discord
        """
        self.format(record)

        desc = [
            record.asctime,
            record.message,
            # record.exc_info,
            # str(record.funcName) + " : " + str(record.lineno),
            # record.stack_info,
        ]

        filtered_desc = [record for record in desc if record != None]

        embed = DiscordEmbed(
            # title="Update",
            description="\n".join(filtered_desc),
            color=242424,
        )
        self.discordWebhook.add_embed(embed)
        self.discordWebhook.execute()
        self.discordWebhook.remove_embed(0)
