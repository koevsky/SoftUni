class Gym:

    def __init__(self):
        self.subscriptions = []
        self.equipment = []
        self.customers = []
        self.trainers = []
        self.plans = []

    def add_customer(self, customer):

        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):

        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):

        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):

        result = []

        subscription = next(filter(lambda s: s.id == subscription_id, self.subscriptions))

        customer_id = subscription.customer_id
        customer = next(filter(lambda c: c.id == customer_id, self.customers))

        trainer_id = subscription.trainer_id
        trainer = next(filter(lambda t: t.id == trainer_id, self.trainers))

        plan_id = subscription.exercise_id
        plan = next(filter(lambda p: p.id == plan_id, self.plans))

        equipment_id = plan.equipment_id
        equipment = next(filter(lambda e: e.id == equipment_id, self.equipment))

        lst = [subscription, customer, trainer, equipment, plan]
        [result.append(str(obj)) for obj in lst]

        return '\n'.join(result)
