def response(hey_bob):
    message = hey_bob.strip()

    # Silence
    if message == "":
        return "Fine. Be that way!"

    # Check if question
    is_question = message.endswith("?")

    # Check if yelling
    has_letters = any(char.isalpha() for char in message)
    is_yelling = has_letters and message.upper() == message

    # Yelling question
    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"

    # Yelling
    if is_yelling:
        return "Whoa, chill out!"

    # Question
    if is_question:
        return "Sure."

    # Anything else
    return "Whatever."