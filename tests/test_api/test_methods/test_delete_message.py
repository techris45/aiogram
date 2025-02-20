from aiogram.methods import DeleteMessage, Request
from tests.mocked_bot import MockedBot


class TestDeleteMessage:
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(DeleteMessage, ok=True, result=True)

        response: bool = await DeleteMessage(chat_id=42, message_id=42)
        request: Request = bot.get_request()
        assert request.method == "deleteMessage"
        assert response == prepare_result.result

    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(DeleteMessage, ok=True, result=True)

        response: bool = await bot.delete_message(chat_id=42, message_id=42)
        request: Request = bot.get_request()
        assert request.method == "deleteMessage"
        assert response == prepare_result.result
