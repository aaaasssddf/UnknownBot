from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from .config import Config

from nonebot import on_command
from nonebot.rule import to_me

__plugin_meta__ = PluginMetadata(
    name="test",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

test_process = on_command("test",rule=to_me())

@test_process.handle()
async def test_function():
    await test_process.finish("111")