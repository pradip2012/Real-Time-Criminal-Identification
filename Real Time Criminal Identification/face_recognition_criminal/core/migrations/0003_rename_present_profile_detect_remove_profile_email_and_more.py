# Generated by Django 4.1.3 on 2023-01-03 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201129_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='present',
            new_name='detect',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profession',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ranking',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='shift',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='status',
        ),
        migrations.AddField(
            model_name='profile',
            name='crime_type',
            field=models.CharField(choices=[('arson', 'arson'), ('assault and battery', 'assault and battery'), ('bribery', 'bribery'), ('burglary', 'burglary'), ('child abuse', 'child abuse'), ('white-collar crime.', 'white-collar crime.'), ('counterfeiting', 'counterfeiting'), ('cybercrime', 'cybercrime'), ('drug use', 'drug use'), ('embezzlement', 'embezzlement'), ('extortion', 'extortion'), ('forgery', 'forgery'), ('fraud', 'fraud'), ('hijacking', 'hijacking'), ('homicide', 'homicide'), ('incest', 'incest'), ('kidnapping', 'kidnapping'), ('larceny', 'larceny'), ('organized crime', 'organized crime'), ('perjury', 'perjury'), ('piracy', 'piracy'), ('prostitution', 'prostitution'), ('rape', 'rape'), ('robbery', 'robbery'), ('sedition', 'sedition'), ('smuggling', 'smuggling'), ('terrorism', 'terrorism'), ('theft', 'theft'), ('treason', 'treason'), ('usury', 'usury')], default='arson', max_length=20, null=True),
        ),
    ]