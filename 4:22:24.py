def remove_all_non_alpha_chars(user):
    return ''.join([c for c in user if c.isalpha()])

def main():
    user = input()
    print(remove_all_non_alpha_chars(user))

main()