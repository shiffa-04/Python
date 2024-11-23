n_english = int(input().strip())
english_subscribers = set(map(int, input().split()))
n_french = int(input().strip())
french_subscribers = set(map(int, input().split()))

unique_subscribers = english_subscribers.union(french_subscribers)

print(len(unique_subscribers))