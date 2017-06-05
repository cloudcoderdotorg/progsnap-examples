# Find the activity with the highest average number of
# submissions per student (omitting instructors)

import sys, progsnap

filename = sys.argv[1]
dataset = progsnap.Dataset(filename)

activity = None
max_subs = 0

for a in dataset.activities():
  total = 0
  for wh in dataset.work_histories_for_activity(a):
    student = dataset.student_for_id(wh.student_id())
    if not student.instructor():
      subs = [e for e in wh.events()
              if type(e) is progsnap.Submission]
      total += len(subs)
  if total > max_subs:
    max_subs = total
    activity = a

print("Activity {}, {} submissions"
      .format(activity.number(), max_subs))
