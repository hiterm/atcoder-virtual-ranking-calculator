import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("json_file")
parser.add_argument("score", type=int)
parser.add_argument("minutes", type=int)
parser.add_argument("seconds", type=int)
args = parser.parse_args()

with open(args.json_file, 'r') as f:
    s = f.read()

score = args.score
minutes = args.minutes
seconds = args.seconds
total_nano_seconds = (minutes * 60 + seconds) * 1000000000
standings = json.loads(s)["StandingsData"]
rank = 1000000000
for st in standings:
    if st["TotalResult"]["Score"] < score * 100:
        rank = st["Rank"]
        break
    elif st["TotalResult"]["Score"] == score * 100 and \
            st["TotalResult"]["Elapsed"] >= total_nano_seconds:
        rank = st["Rank"]
        break

print(rank)
