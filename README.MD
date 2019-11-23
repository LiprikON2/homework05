# Telegram schedule bot

- Fetches ITMO University's schedule for specific group

## Bot commands

#### Specific day: `/WEEKDAY GROUP`
*e.g.*
```
/monday k3140
```

#### All week: `/all PARITY GROUP`
##### PARITY: 
`1` for even week schedule
`2` for odd week schedule
`0` for both

*e.g.*
```
/all 0 k3140
```

#### Tomorrow: `/tomorrow GROUP`

*e.g.*
```
/tomorrow k3140
```

#### Next class: `/near GROUP`

*e.g.*
```
/near k3140
```

## Setup


1. Create config.py with following content
```python
# Telegram bot's api token
access_token = 'XXXXXXXXXXXXXXXXXX'
domain = 'http://www.ifmo.ru/ru/schedule/0'
```
2. `pip install requirements.txt`
3. `python bot.py`