# Generated by Django 4.1.5 on 2023-05-22 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_present_profile_detect_remove_profile_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='fir',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='crime_type',
            field=models.CharField(choices=[('arson', 'arson'), ('assault and battery', 'assault and battery'), ('bribery', 'bribery'), ('burglary', 'burglary'), ('child abuse', 'child abuse'), ('white-collar crime.', 'white-collar crime.'), ('counterfeiting', 'counterfeiting'), ('cybercrime', 'cybercrime'), ('drug use', 'drug use'), ('embezzlement', 'embezzlement'), ('extortion', 'extortion'), ('forgery', 'forgery'), ('fraud', 'fraud'), ('hijacking', 'hijacking'), ('homicide', 'homicide'), ('incest', 'incest'), ('kidnapping', 'kidnapping'), ('larceny', 'larceny'), ('organized crime', 'organized crime'), ('perjury', 'perjury'), ('piracy', 'piracy'), ('prostitution', 'prostitution'), ('rape', 'rape'), ('robbery', 'robbery'), ('sedition', 'sedition'), ('smuggling', 'smuggling'), ('terrorism', 'terrorism'), ('theft', 'theft'), ('treason', 'treason'), ('usury', 'usury'), ('missing person', 'missing person')], default='arson', max_length=20, null=True),
        ),
    ]
