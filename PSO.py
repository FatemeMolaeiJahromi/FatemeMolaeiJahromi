import random
import numpy as np

# تابع ارزیابی که باید بهینهسازی شود
def evaluate_gearbox_design(solution):
    # این تابع باید مدل دقیق گیربکس را ارزیابی کند
    # برای مثال، ما یک تابع ساده را شبیه‌سازی می‌کنیم
    return sum((x - 5) ** 2 for x in solution)

# الگوریتم PSO
def pso(num_particles, num_dimensions, num_iterations):
    # مقداردهی اولیه
    particle_position = np.random.rand(num_particles, num_dimensions)
    particle_velocity = np.random.rand(num_particles, num_dimensions)
    personal_best_position = np.copy(particle_position)
    personal_best_value = np.array([float('inf') for _ in range(num_particles)])
    # بهترین جهانی
    global_best_value = float('inf')
    global_best_position = np.zeros(num_dimensions)

    for iteration in range(num_iterations):
        for i in range(num_particles):
            # ارزیابی ذره
            current_value = evaluate_gearbox_design(particle_position[i])
            # به‌روزرسانی بهترین شخصی
            if current_value < personal_best_value[i]:
                personal_best_value[i] = current_value
                personal_best_position[i] = particle_position[i]
                # به‌روزرسانی بهترین جهانی
                if current_value < global_best_value:
                    global_best_value = current_value
                    global_best_position = particle_position[i]
            # به‌روزرسانی سرعت و موقعیت
            inertia_weight = 0.5
            cognitive_weight = 1
            social_weight = 1
            particle_velocity[i] = (inertia_weight * particle_velocity[i] +
                                    cognitive_weight * random.random() * 
                                    (personal_best_position[i] - particle_position[i]) +
                                    social_weight * random.random() * 
                                    (global_best_position - particle_position[i]))
            particle_position[i] += particle_velocity[i]

        # نمایش پیشرفت
        print(f'Iteration {iteration}: Best Value = {global_best_value}')

    return global_best_position

# تنظیمات الگوریتم
num_particles = 30
num_dimensions = 5
num_iterations = 100

# اجرای الگوریتم
best_position = pso(num_particles, num_dimensions, num_iterations)
print(f'Best Position: {best_position}')