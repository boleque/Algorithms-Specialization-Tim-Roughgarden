#This file describes a set of jobs with positive and integral weights and lengths.  It has the format
#
#[number_of_jobs]
#
#[job_1_weight] [job_1_length]
#
#[job_2_weight] [job_2_length]
#
#
#For example, the third line of the file is "74 59", indicating that the second job has weight 74 and length 59.
#You should NOT assume that edge weights or lengths are distinct.

#Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of 
# 1. the difference (weight - length)
# 2. the ratio weight/length.  
#Recall from lecture that this algorithm is not always optimal.  IMPORTANT: if two jobs have equal difference (weight - length), 
#you should schedule the job with higher weight first.  Beware: if you break ties in a different way, you are likely to get the wrong answer.  
#You should report the sum of weighted completion times of the resulting schedule


def get_jobs():
    jobs = []
    jobs_num = 0
    with open('jobs.txt') as f:
        lines = iter(f.readlines())
        jobs_num = int(next(lines))
        for line in lines:
            jobs.append(
                [int(v) for v in line.split()] #[job_1_weight] [job_1_length]
            )
    return jobs_num, jobs

def weighted_completion_times(jobs_num, jobs, score_type):
    # sort criterias:
    # 1. decreasing order according to score type
    # 2. job with higher weight first
    if score_type == 'ratio':
        sort_criteria = lambda job_info: (float(job_info[0])/job_info[1], job_info[0])
    elif score_type == 'difference':
        sort_criteria = lambda job_info: (job_info[0] - job_info[1], job_info[0])

    jobs_num_sorted = sorted(jobs, key=sort_criteria, reverse=True)
    completion_times = 0
    total_time = 0
    for weight, length in jobs_num_sorted:
        total_time += length
        completion_times += weight * total_time
    return completion_times

if __name__ == '__main__':
    jobs_num, jobs = get_jobs()
    score_types = 'ratio', 'difference'

    for score_type in score_types:
        completion_times = weighted_completion_times(jobs_num, jobs, score_type)
        print('for score type={} / completion times is={}'.format(score_type, completion_times))

# for score type=ratio / completion times is=67311454237
# for score type=difference / completion times is=69119377652