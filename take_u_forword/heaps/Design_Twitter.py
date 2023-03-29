"""
https://leetcode.com/problems/design-twitter/description/
"""
from collections import deque
import heapq
from typing import List


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cnt = 0 # global counter
        self.tweets = {} # mapping from user to tweets
        self.followers = {} # mapping from user to followers

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.cnt += 1
        self.tweets.setdefault(userId, deque()).appendleft((self.cnt, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        hp = [] # max heap
        for fid in self.followers.get(userId, set()) | {userId}:
            if fid in self.tweets: # has tweeted
                cnt, tid = self.tweets[fid][0]
                heapq.heappush(hp, (-cnt, tid, fid, 0)) # push follower's tweet on heap
        ans = []
        for _ in range(10):
            if not hp: break
            _, tid, uid, i = heapq.heappop(hp)
            ans.append(tid)
            if i+1 < len(self.tweets[uid]):
                cnt, tid = self.tweets[uid][i+1]
                heapq.heappush(hp, (-cnt, tid, uid, i+1))
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followers.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followers.setdefault(followerId, set()).discard(followeeId)

# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(userId=1,tweetId=5)
print(obj.getNewsFeed(userId=1))
obj.follow(followerId=1, followeeId=2)
obj.unfollow(followerId=2, followeeId=6)
print(obj.getNewsFeed(userId=1))
obj.follow(followerId=1, followeeId=2)
print(obj.getNewsFeed(userId=1))