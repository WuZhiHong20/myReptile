from pybloom_live import BloomFilter


def init_bloom(size=2e8):
    bloom = BloomFilter(capacity=size)
    return bloom
