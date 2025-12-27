def calculate_positive_feedback_percentage(ratings):
    # Handle case where no ratings are available
    if not ratings:
        return 0

    positive_count = sum(1 for rating in ratings if rating >= 4)
    percentage = (positive_count / len(ratings)) * 100

    return round(percentage, 2)

ratings = [5, 4, 3, 5, 2, 4, 1, 5]

positive_feedback = calculate_positive_feedback_percentage(ratings)

print(f"Positive Feedback: {positive_feedback}%")
