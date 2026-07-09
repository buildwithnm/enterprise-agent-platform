from app.chains.chat_chain import ChatChain


def test_chain_creation():

    chain = ChatChain.build("general")

    assert chain is not None
