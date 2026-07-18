from datetime import datetime
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnableBranch,
    RunnablePassthrough,
)

clean_question = RunnableLambda(
    lambda x: x["question"].strip()
)

RunnablePassthrough.assign(
    timestamp=lambda _: datetime.utcnow().isoformat()
)

RunnablePassthrough.assign(
    word_count=lambda x: len(
        x["question"].split()
    )
)

# parallel = RunnableParallel(
#     summary=summary_chain,
#     keywords=keyword_chain,
# )

# RunnableBranch(

#     (
#         lambda x:
#         x["persona"] == "general",

#         general_chain,
#     ),

#     (
#         lambda x:
#         x["persona"] == "data_engineer",

#         data_engineer_chain,
#     ),

#     default_chain,
# )