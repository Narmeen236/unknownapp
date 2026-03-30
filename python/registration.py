class EnrollmentManager:
    """
    Re-engineered Python version of the Course Registration Use Case.
    Focuses on business rule validation: Capacity, Prerequisites, and Duplicates.
    """
    def __init__(self):
        # Mocking the system state based on the Java implementation
        self.catalog = {
            "CS101": {"name": "Intro to Programming", "capacity": 30, "enrolled": 30, "req": []},
            "CS201": {"name": "Data Structures", "capacity": 25, "enrolled": 15, "req": ["CS101"]},
            "CS301": {"name": "Algorithms", "capacity": 20, "enrolled": 5, "req": ["CS201"]}
        }
        # Mock student data
        self.completed_courses = ["CS101"]
        self.current_registration = []

    def process_registration(self, code):
        print(f"\n[System] Processing registration for course: {code}")
        
        course = self.catalog.get(code)
        
        # Validation 1: Existence check
        if not course:
            return f"Error: Course code {code} not found in catalog."

        # Validation 2: Duplicate check
        if code in self.current_registration:
            return f"Error: You are already registered for {code}."

        # Validation 3: Capacity check
        if course['enrolled'] >= course['capacity']:
            return f"Error: {code} is full ({course['enrolled']}/{course['capacity']})."

        # Validation 4: Prerequisite check
        for req in course['req']:
            if req not in self.completed_courses:
                return f"Error: Prerequisite '{req}' not satisfied for {code}."

        # Process enrollment
        self.current_registration.append(code)
        course['enrolled'] += 1
        return f"Success: Enrolled in {code} - {course['name']}."

if __name__ == "__main__":
    app = EnrollmentManager()
    
    # Demonstration of different scenarios
    print(app.process_registration("CS201")) # Should succeed
    print(app.process_registration("CS101")) # Should fail (Full)
    print(app.process_registration("CS301")) # Should fail (Prereq not met)