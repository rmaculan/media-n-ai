# Generated by Django 5.1.1 on 2025-04-03 20:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("blog", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "notification_types",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "Like"),
                            (2, "Comment"),
                            (3, "Follow"),
                            (4, "Message"),
                        ],
                        null=True,
                    ),
                ),
                ("text_preview", models.CharField(blank=True, max_length=100)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("is_seen", models.BooleanField(default=False)),
                (
                    "post",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_notification",
                        to="blog.post",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sender_notification",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_notification",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
