def format_sse(
    data: str,
    event: str = "message",
):

    return f"event: {event}\n" f"data: {data}\n\n"
