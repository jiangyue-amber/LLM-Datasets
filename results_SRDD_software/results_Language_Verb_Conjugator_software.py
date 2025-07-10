# Software Name: Language_Verb_Conjugator
# Category: Language
# Description: Language Verb Conjugator is a software application that helps language learners practice and improve their verb conjugation skills. It provides a comprehensive database of verbs in various languages along with their conjugation patterns. Users can search for a specific verb and the software will display its conjugations in different tenses, moods, and persons. The conjugations are presented in a clear and organized format, making it easy for users to study and practice verb conjugation.

class VerbConjugator:
    def __init__(self, language):
        self.language = language
        self.verb_data = {}  # Dictionary to store verb conjugations

    def load_verb_data(self, data):
        """Loads verb conjugation data from a dictionary."""
        self.verb_data = data

    def conjugate(self, verb, tense, mood, person):
        """
        Conjugates a verb for a given tense, mood, and person.

        Args:
            verb (str): The verb to conjugate.
            tense (str): The tense to conjugate in (e.g., "present", "past").
            mood (str): The mood to conjugate in (e.g., "indicative", "subjunctive").
            person (str): The person to conjugate in (e.g., "1st person singular", "2nd person plural").

        Returns:
            str: The conjugated verb form, or None if not found.
        """
        if verb in self.verb_data and tense in self.verb_data[verb] and mood in self.verb_data[verb][tense] and person in self.verb_data[verb][tense][mood]:
            return self.verb_data[verb][tense][mood][person]
        else:
            return None

    def get_conjugations(self, verb):
        """
        Retrieves all conjugations for a given verb.

        Args:
            verb (str): The verb to retrieve conjugations for.

        Returns:
            dict: A dictionary containing all conjugations for the verb, or None if not found.
        """
        if verb in self.verb_data:
            return self.verb_data[verb]
        else:
            return None

    def search_verb(self, verb):
        """Searches for a verb in the database.
        Args:
            verb (str): The verb to search for.

        Returns:
            bool: True if the verb is found, False otherwise.
        """
        return verb in self.verb_data

# Example usage (sample data):
if __name__ == '__main__':
    conjugator = VerbConjugator("Spanish")
    sample_data = {
        "hablar": {
            "present": {
                "indicative": {
                    "1st person singular": "hablo",
                    "2nd person singular": "hablas",
                    "3rd person singular": "habla",
                    "1st person plural": "hablamos",
                    "2nd person plural": "habláis",
                    "3rd person plural": "hablan"
                },
                "subjunctive": {
                     "1st person singular": "hable",
                    "2nd person singular": "hables",
                    "3rd person singular": "hable",
                    "1st person plural": "hablemos",
                    "2nd person plural": "habléis",
                    "3rd person plural": "hablen"
                }
            },
            "past": {
                "indicative": {
                    "1st person singular": "hablé",
                    "2nd person singular": "hablaste",
                    "3rd person singular": "habló",
                    "1st person plural": "hablamos",
                    "2nd person plural": "hablasteis",
                    "3rd person plural": "hablaron"
                }
            }
        }
    }
    conjugator.load_verb_data(sample_data)

    # Example: Conjugate "hablar" in the present indicative, 1st person singular
    conjugated_verb = conjugator.conjugate("hablar", "present", "indicative", "1st person singular")
    if conjugated_verb:
        print(f"The conjugation is: {conjugated_verb}")  # Output: The conjugation is: hablo
    else:
        print("Conjugation not found.")

    # Example: Get all conjugations for "hablar"
    all_conjugations = conjugator.get_conjugations("hablar")
    if all_conjugations:
        print(f"All conjugations for 'hablar': {all_conjugations}")
    else:
        print("Verb not found.")

    # Example: Search for verb
    verb_to_search = "hablar"
    if conjugator.search_verb(verb_to_search):
        print(f"The verb '{verb_to_search}' was found.")
    else:
        print(f"The verb '{verb_to_search}' was not found.")