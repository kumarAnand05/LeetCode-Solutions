select users.name, sum(transactions.amount) as balance
from transactions join users
on users.account=transactions.account
group by transactions.account
having balance > 10000
