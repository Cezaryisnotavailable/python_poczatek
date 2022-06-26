import random

def run_example():
  expenditures_name = ["prąd", "woda", "zakupy"]
  expenditures = {expenditure_name: random.randint(1, 100) for expenditure_name in expenditures_name}
  print(expenditures)
  expenditures = {random.randint(1, 100): expenditure_name for expenditure_name in expenditures_name}
  print(expenditures)


  studend_names = ["Alicjayyyy", "Robert", "Mikołaj", "Gierwazyy"]
  students = {random.randint(1, 100): name for name in studend_names if len(name) < 8}
  print(students)

  #inny przykład
  students = {
    random.randint(1, 100): name if len(name) < 8 else f"{name[:5]}..."
    for name in studend_names
  }
  print(students)


if __name__ == "__main__":
    run_example()
