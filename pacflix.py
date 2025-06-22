from tabulate import tabulate


class User:

    service_database = {
        "Basic Plan": [True, True, True, False, False, 1, "3rd party Movie only", 120_000],
        "Standard Plan": [True, True, True, True, False, 2, "Basic Plan Content + Sports", 160_000],
        "Premium Plan": [True, True, True, True, True, 4, "Basic Plan + Standard Plan + PacFlix Original Series", 200_000],
        "Services": ["Can Stream", "Can Download", "SD Quality", "HD Quality", "UHD Quality", "Number of Devices", "Content Type", "Price"]
    }

    def __init__(self, username):
        self.username = username


    def check_benefit(self):
        """Display a table of all available PacFlix plans."""
        services_table = tabulate(User.service_database, headers="keys")
        print("PacFlix Plan List")
        print(" ")
        print(services_table)


class ExistingUser(User):

    def __init__(self, username, duration_plan, current_plan):
        super().__init__(username)

        # Ensure duration input is not negative
        if duration_plan < 0:
            raise ValueError("Invalid duration. Duration cannot be negative.")
        self.duration_plan = duration_plan

        # Ensure current_plan is available in service_database
        if current_plan not in [key for key in User.service_database.keys() if key != "Services"]:
            raise TypeError(f"{current_plan} is not listed in our database. Please choose 'Basic Plan', 'Standard Plan', or 'Premium Plan'.")
        self.current_plan = current_plan


    def check_plan(self):
        """Display the current plan details."""
        if self.duration_plan == 0:
            print(f"Currently, you are subscribed to {self.current_plan}.")
        else:
            print(f"You have been subscribed to {self.current_plan} for {self.duration_plan} months.")

        print(f" ")

        check_plan = User.service_database.copy()
        for plan, value in User.service_database.items():
            if plan not in [self.current_plan, "Services"]:
                check_plan.pop(plan)
        check_plan_table = tabulate(check_plan, headers="keys")
        print(check_plan_table)


    def upgrade_plan(self, new_plan):
        """
        Calculate the total cost of upgrading the subscription.

        Parameters:
            - new_plan (str): The new plan selected.

        Rules:
            - Can only upgrade to a higher plan.
            - 5% discount if subscribed for more than 12 months.

        Output:
            - A message stating the new active plan & total payment
            - Updates current_plan -> new_plan
            - Resets duration_plan -> 0
        """
        discount = 0.0
        grading = {
            key:index for index, (key, value) in enumerate(User.service_database.items()) if key != "Services"
        }

        # Ensure new_plan is available in service_database
        if new_plan not in grading.keys():
            raise TypeError("You can only upgrade to 'Standard Plan' or 'Premium Plan'.")

        # Ensure the user upgrades and not downgrades plan by using grading
        if grading[new_plan] <= grading[self.current_plan]:
            raise TypeError(f"You are currently subscribed to {self.current_plan}. You may only upgrade to a higher-tier plan.")

        if self.duration_plan > 12:
            discount = 0.05
        else:
            discount = 0.0

        cut_price = User.service_database[new_plan][-1] * discount
        final_price = User.service_database[new_plan][-1] - (cut_price)

        print(f"Thank you! Your {new_plan} plan is now active.")
        print(" ")
        if discount > 0.0:
            print(f"You received a discount of Rp {cut_price: .2f}")
            print(f"because you had been subscribed to {self.current_plan} for more than 12 months.")
            print(" ")
        print(f"The total amount you paid is Rp {final_price: .2f}")

        self.current_plan = new_plan
        self.duration_plan = 0


class NewUser(User):

    def __init__(self, username):
        super().__init__(username)

    def __valid_referral(self, data=None):
        """
        Private method to define valid_referral, used internally by pick_plan()

        Purpose:
            The variable 'data' (containing referral codes) is external,
            which may pose a risk if compromised.

            This method safely stores initial referral codes in an internal list.
            If the format of 'data' is valid, this method appends it to the internal database.
            Otherwise, it catches the exception and continues using only the initial list.
        """
        # Storage for initial referral codes
        initial_referral = [
            "shandy-2134", "cahya-abcd",
            "ana-2f9g", "bagus-9f92"
        ]

        valid_referral = initial_referral.copy()

        # Ensure 'data' type is dictionary and not empty
        if isinstance(data, dict) and data:
            try:
                for record in data.values():
                    if record[-1] not in valid_referral:
                        valid_referral.append(record[-1])
            except (AttributeError, ValueError):
                print("Referral data error: Please ensure your external data variable is dictionary with 'Name' as key and values of a list formatted like ['Plan Name', duration, 'referral-code']")

        # Returning 'initial_referral' in case error occured when appending 'valid_referral'
        try:
            return valid_referral
        except Exception:
            print("Error while processing referral list. Using initial default referral list.")
            return initial_referral


    def pick_plan(self, new_plan, referral_code="no ref", data=None):
        """
        Calculate the total cost of registering for a new plan.

        Parameters:
            - new_plan (str): Selected plan.
            - referral_code (str): Optional referral code; default is "no ref".
            - data (dict): Optional additional valid refferal code database; default is None.

        Rules:
            - 4% discount if referral code is valid.

        Output:
            - Message stating the activated plan and total payment.
        """
        discount = 0.0
        valid_referral = self.__valid_referral(data=data)

        # Ensure new_plan is available in service_database
        if new_plan not in [key for key in User.service_database.keys() if key != "Services"]:
            raise TypeError("Please choose between 'Basic Plan', 'Standard Plan', or 'Premium Plan'")

        if referral_code == "no ref":
            discount = 0.0

        elif referral_code not in valid_referral:
            raise NameError("Referral code not found. Leave it blank if you don’t have one.")
        else:
            print("Referral code accepted!")
            discount = 0.04

        cut_price = User.service_database[new_plan][-1] * discount
        final_price = User.service_database[new_plan][-1] - cut_price

        print(f"Thank you! Your {new_plan} plan is now active.")
        print(" ")
        if discount > 0.0:
            print(f"You received a discount of Rp {cut_price: .2f}")
            print("because you used a valid referral code.")
            print(" ")
        print(f"The total amount you paid is Rp {final_price: .2f}")