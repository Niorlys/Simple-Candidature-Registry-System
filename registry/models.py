from django.db import models
from django.core.exceptions import ValidationError


__all__ = ["Candidate", "CandidateTechs", "Technology"]
# Validators
def validate_ci(ci):
    if not ci.isnumeric() or len(ci) != 11:
        raise ValidationError(f"{ci} no es un numero de identidad valido. Debe ser un numero de 11 digitos")
    if ci[:2] < "88":
        raise ValidationError("El candidato ha de tener una edad menor a 35")

def validate_age(value):
    if value > 35:
        raise ValidationError("El candidato ha de tener una edad menor a 35")




class Candidate(models.Model):
    candidate_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    ci = models.CharField(max_length=20,validators=[validate_ci], unique=True)
    address = models.CharField(max_length= 100)
    age = models.IntegerField(validators=[validate_age])
    sex = models.CharField(max_length=1, choices=(('M','Maculino'), ('F', 'Femenino')))
    techs = models.ManyToManyField("Technology",related_name="techs", through="CandidateTechs")

    def __str__(self) -> str:
        return f"Candidato {self.candidate_id}: {self.name} {self.last_name}"


class Technology(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"Tecnologia: {self.name}"

class CandidateTechs(models.Model):
    candidate = models.ForeignKey("Candidate",on_delete=models.CASCADE)
    tech = models.ForeignKey("Technology",on_delete=models.CASCADE)

    experience = models.IntegerField(null=True)






