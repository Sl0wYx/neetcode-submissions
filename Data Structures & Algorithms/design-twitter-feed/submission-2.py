class Twitter:

    def __init__(self):
        self.count = 0
        self.follows = defaultdict(set)
        self.posts = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        self.follows[userId].add(userId)
        for followeeId in self.follows[userId]:
            if followeeId in self.posts:
                index = len(self.posts[followeeId]) - 1
                count, tweetId = self.posts[followeeId][index]
                min_heap.append([count, tweetId, followeeId, index - 1])

        heapq.heapify(min_heap)

        while min_heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.posts[followeeId][index]
                heapq.heappush(min_heap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
