#!/usr/bin/env python3
# funniest-ai-out-of-office-reply — round 3 entry.
# A one-line out-of-office reply, as the bounty requires.
# The joke: the request is forwarded to a future self
# who is just as unhelpful as the present one.
# The reply is a single sentence pair, printed once.
# Nothing is read from input and nothing else is shown.
# The text is assembled from two short parts, joined
# with a single space, so the line stays readable here.
# The main function prints the assembled line exactly.
# (Round 3 rewrite: new reply, same one-line output contract.)


def main():
    opening = "Thank you for your email."
    body = "I am out of office and have forwarded your request to my future self, who is also ignoring it."
    print(opening + " " + body)


if __name__ == "__main__":
    main()
