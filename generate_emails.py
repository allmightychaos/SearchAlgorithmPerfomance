import random
import string

# Email domains to use
domains = [
    "@gmail.com", "@yahoo.com", "@outlook.com", "@hotmail.com", "@icloud.com",
    "@aol.com", "@protonmail.com", "@zoho.com", "@mail.com", "@yandex.com"
]

def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(5, 10)))
    domain = random.choice(domains)
    return username + domain

def generate_email_list(count):
    email_list = []
    for i in range(1, count + 1):
        email_list.append(generate_random_email())
        if i % 10000 == 0:  # Print progress every 10,000 emails
            percentage_done = (i / count) * 100
            print(f"{percentage_done:.2f}% - {i} emails generated...")
    return email_list

if __name__ == "__main__":
    total_emails = 5000000  # Number of emails to generate
    email_list = generate_email_list(total_emails)
    
    with open("emails.txt", "w") as f:
        f.write("\n".join(email_list))
    
    print("Email generation completed.")
    print("Sample emails:", email_list[:10])
