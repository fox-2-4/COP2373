# COP 2373
# Programming Exercise 2
# Brayden Fox

# import re


def main():
    # collect email message input from user
    # make it lowercase to make the hit detection case-insensitive
    email_message = input()
    email_message = email_message.lower()

    # initialize the spam count and get tuple of spam phrases
    spam_count = 0
    spam_phrases = get_spam_phrases()
    # stores the detected phrases
    spam_hits: list[str] = []

    # search the message for each phrase in the list
    for phrase in spam_phrases:
        # use str.count() to count the number of non-overlapping occurrences of each spam phrase
        ct = email_message.count(phrase.lower())
        # when the count is non-zero, append the offending phrase and up the spam counter
        if ct > 0:
            spam_hits.append(phrase)
            spam_count += ct

    # display the output to the console
    if spam_count > 0:
        print(f"Message spam score: {spam_count}")
        # give a likelihood estimation of spam
        if spam_count < 2:
            print("This message may be spam.")
        elif spam_count < 4:
            print("This message is likely spam.")
        else:
            print("This message is very likely spam.")

        print(f"Offending phrases discovered: {spam_hits}")

    else:
        print("No spam phrases discovered.")


# returns a tuple of 30 spam phrases
def get_spam_phrases() -> tuple[str, ...]:
    return (
        "Free money",
        "Cash bonus",
        "Get paid",
        "Make money",
        "Earn extra cash",
        "Unlimited income",
        "Fast cash",
        "Financial freedom",
        "Work from home",
        "Act now",
        "Urgent",
        "Limited time",
        "Don’t miss out",
        "Hurry",
        "Final notice",
        "Instant access",
        "Exclusive deal",
        "Risk-free",
        "No hidden fees",
        "Guaranteed",
        "100% free",
        "No catch",
        "You have been selected",
        "Congratulations",
        "Click below",
        "Lowest price",
        "Best price",
        "Sale now",
        "Discount",
        "Buy direct",
        "Order now",
    )


# execute main program
if __name__ == "__main__":
    main()
