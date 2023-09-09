select machine_id, round(2*avg(
  CASE
  when activity_type = 'start' then -timestamp
  else timestamp
  end
),3) as processing_time from activity
group by machine_id
