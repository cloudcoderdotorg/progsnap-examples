# Find the activity with the highest average number of
# submissions per student (omitting instructors)

import sys, progsnap

filename = sys.argv[1]
dataset = progsnap.Dataset(filename)

activity = None
highest_avg = 0

for a in dataset.activities():
  total = 0
  n = 0
  for wh in dataset.work_histories_for_activity(a):
    student = dataset.student_for_id(wh.student_id())
    if not student.instructor():
      subs = [e for e in wh.events()
              if type(e) is progsnap.Submission]
      total += len(subs)
      n += 1
  avg = total / n
  if avg > highest_avg:
    activity = a
    highest_avg = avg

print("Activity {}, {} submissions/student"
      .format(activity.number(), highest_avg))

# Note that the formatting of this file is somewhat
# awkward because it was used in a poster where space
# was at a premium.
