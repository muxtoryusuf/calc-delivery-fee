from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=256)
    zone = models.SmallIntegerField(default=1)  # zone 1, 2, 3 ... etc

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"
        ordering = ['-id']

    def __str__(self):
        return f"{self.name}: {self.zone}"


class Dimension(models.Model):
    width = models.FloatField(default=0.0, help_text="CM \nШирина / Kenglik")
    length = models.FloatField(default=0.0, help_text="CM \nДлина / Uzunlig")
    height = models.FloatField(default=0.0, help_text="CM \nВысота / Balandlik")
    cube = models.FloatField(default=0.0, help_text="Cube: (This field is written automatically)")

    class Meta:
        verbose_name = "Dimension"
        verbose_name_plural = "Dimensions"
        ordering = ['-id']

    def __str__(self):
        return f"Cube: {self.cube}"

    def save(self, *args, **kwargs):
        volume = (self.width * self.length * self.height)
        self.cube = volume / 1000000
        super(Dimension, self).save(*args, **kwargs)


class Tariff(models.Model):
    name = models.CharField(max_length=120)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    min_weight = models.FloatField(default=0.0)
    max_weight = models.FloatField(default=0.0)
    dimension = models.ForeignKey(Dimension, help_text="Cubic meter: м3", on_delete=models.CASCADE)
    total = models.FloatField(default=0.0)  # 25 800 sum

    class Meta:
        verbose_name = "Tariff"
        verbose_name_plural = "Tariffs"
        ordering = ['-id']

    def __str__(self):
        return f"{self.name}"

