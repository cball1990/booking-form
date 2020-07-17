from django.db import models

GameChoices = [
('40k','40K'),
('40kcrusade','40K Crusade'),
('30k ','30K'),
('killteam','KillTeam'),
('titanicus','Titanicus'),
('aos','AOS'),
('warcry','Warcry'),
('underworlds','Underworlds'),
('necromunda','Necromunda'),
('other','Other')
]
SkillChoices = [
    ('beginner','Beginner'),
    ('intermediate', 'Intermediate'),
    ('pro','Pro'),
    ('absolute cheese master 9000', 'Absolute Cheese Master 9000')
]
class BookTable(models.Model):
    name = models.CharField(max_length=30)
    gametype = models.CharField(max_length=50, choices=GameChoices, default='40k')
    points = models.IntegerField()
    skilllevel = models.CharField(max_length=50, choices=SkillChoices, default='begginer')
    opponent = models.CharField(max_length=100)
    army = models.CharField(max_length=200)

