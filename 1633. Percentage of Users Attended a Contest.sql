select contest_id, round(100*count(register.user_id)/(select count(*) from users),2) as percentage from register
left join users
on register.user_id = users.user_id
group by contest_id
order by percentage desc, contest_id
