class User:

  plans_data = {
        "Basic Plan": [True, True, True, False, False, 1, "3rd party Movie only", 120_000],
        "Standard Plan": [True, True, True, True, False, 2, "Basic Plan Content + Sports", 160_000],
        "Premium Plan": [True, True, True, True, True, 4, "Basic Plan + Standard Plan + PacFlix Original Series", 200_000],
        "Services": ["Bisa Stream", "Bisa Download", "Kualitas SD", "Kualitas HD", "Kualitas UHD", "Number of Devices", "Jenis Konten", "Harga"]
    }

  def __init__(self, username, duration_plan, current_plan):
    self.username = username
    self.duration_plan = duration_plan
    self.current_plan = current_plan

  def check_benefit(self):
    all_plans_table = tabulate(User.plans_data, headers="keys")
    print(all_plans_table)

  def check_plan(self, username):
    print(self.current_plan)
    print(f"{self.duration_plan} Bulan")
    print(" ")

    check_plan = User.plans_data.copy()

    for key, index in User.plans_data.items():
      if key not in [self.current_plan, "Services"]:
        check_plan.pop(key)
    current_plan_table = tabulate(check_plan, headers="keys")
    print(current_plan_table)

  def upgrade_plan(self, username, new_plan):
    diskon = 0
    grading = {
        "Basic Plan": 0,
        "Standard Plan": 1,
        "Premium Plan": 2
    }

    if username not in self.username:
      raise NameError("Anda salah memasukkan username")

    if new_plan not in grading.keys():
      raise NameError("New Plan yang bisa Anda pilih hanya 'Standard Plan' atau 'Premium Plan'")

    if grading[new_plan] <= grading[self.current_plan]:
      raise TypeError(f"Plan saat ini: {self.current_plan}. Anda hanya boleh upgrade ke plan yang lebih tinggi")

    else:
      if self.duration_plan > 12:
        diskon = 0.05 * User.plans_data[new_plan][-1]
      else:
        diskon = 0 * User.plans_data[new_plan][-1]

    return User.plans_data[new_plan][-1] - diskon


class NewUser:

  existing_user = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
  }
  def __init__(self, username):
    self.username = username

  def check_benefit(self):
    return User.check_benefit(self)

  def pick_plan(self, new_plan, referral_code="No ref"):
    diskon = 0
    valid_referral = []

    for key, record in NewUser.existing_user.items():
      valid_referral.append(record[-1])

    if new_plan not in User.plans_data.keys():
      raise NameError("Silakan memilih di antara: 'Basic Plan', 'Standard Plan' atau 'Premium Plan'")

    if referral_code == "No ref":
      diskon = 0 * User.plans_data[new_plan][-1]

    else:
      if referral_code not in valid_referral:
        raise NameError("Referral code doesn't exist. Just leave it empty if you don't have one")
      else:
        print("Referral code exist")
        diskon = 0.04 * User.plans_data[new_plan][-1]

    return User.plans_data[new_plan][-1] - diskon