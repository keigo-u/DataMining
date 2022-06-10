from quilt.data.haradai1262 import YouTuber
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#df = YouTuber.channels.UUUM()
df = YouTuber.channel_videos.UUUM_videos()

# check the descriptive statistics of numerical data
df["dislikeCount"].hist(bins=50)
plt.show()