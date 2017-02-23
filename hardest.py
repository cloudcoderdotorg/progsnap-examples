"""
Usage:
  hardest.py <dataset>
"""

# Find the activity with the highest average number of submissions
# per student.

import progsnap

if __name__ == '__main__':
  from docopt import docopt
  arguments = docopt(__doc__)
  datazip = arguments.get("<dataset>")

  dataset = progsnap.Dataset(datazip)

  activities = dataset.activities()

  activity = None
  highest_avg = 0

  for a in activities:
    work_histories = dataset.work_histories_for_activity(a)
    total = 0
    n = 0
    for wh in work_histories:
      subs = [e for e in wh.events() if type(e) is progsnap.Submission]
      total += len(subs)
      n += 1
    avg = total / n
    if avg > highest_avg:
      activity = a
      highest_avg = avg

  print("Activity {} has highest average submissions/student ({})"
        .format(a.number(), highest_avg))

# vim:set expandtab:
# vim:set tabstop=2:
