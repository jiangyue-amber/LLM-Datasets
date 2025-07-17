# Software Name: CustomFit
# Category: Shopping
# Description: CustomFit is a shopping software application that helps users find clothing and accessories that are tailored to their specific body measurements and personal style. It provides a seamless shopping experience by offering a curated collection of products that are available in various sizes and customizable options. Users can input their body measurements and style preferences, and the software will recommend items that are the best fit for them. CustomFit aims to eliminate the hassle of finding the right size and style, ultimately saving users time and ensuring satisfaction with their purchases.

class CustomFit:
    def __init__(self):
        self.user_measurements = {}
        self.user_style_preferences = []
        self.product_catalog = []

    def set_user_measurements(self, measurements):
        """
        Sets the user's body measurements.

        Args:
            measurements (dict): A dictionary of body measurements, e.g., {"chest": 38, "waist": 32, "hips": 40}.
        """
        self.user_measurements = measurements

    def set_user_style_preferences(self, preferences):
        """
        Sets the user's style preferences.

        Args:
            preferences (list): A list of style preferences, e.g., ["casual", "modern", "bohemian"].
        """
        self.user_style_preferences = preferences

    def add_product(self, product):
        """
        Adds a product to the product catalog.

        Args:
            product (dict): A dictionary representing a product, including details such as size availability,
                            customizable options, style, and measurements.
        """
        self.product_catalog.append(product)

    def recommend_items(self):
        """
        Recommends items from the product catalog based on the user's measurements and style preferences.

        Returns:
            list: A list of recommended product dictionaries.
        """
        recommendations = []
        for product in self.product_catalog:
            if self.is_good_fit(product) and self.matches_style(product):
                recommendations.append(product)
        return recommendations

    def is_good_fit(self, product):
        """
        Checks if a product is a good fit for the user based on their measurements.

        Args:
            product (dict): A product dictionary.

        Returns:
            bool: True if the product is a good fit, False otherwise.  Assumes product dictionary contains keys related to relevant measurements.
        """
        if not self.user_measurements:
            return True # Consider it a good fit if no user measurements provided. Can be configured to return false.

        #Simple fit check: compare chest/waist if available
        if 'chest' in self.user_measurements and 'chest_size' in product:
            if abs(self.user_measurements['chest'] - product['chest_size']) > 2: #within 2 inches
                return False
        if 'waist' in self.user_measurements and 'waist_size' in product:
            if abs(self.user_measurements['waist'] - product['waist_size']) > 2:
                return False

        return True

    def matches_style(self, product):
        """
        Checks if a product matches the user's style preferences.

        Args:
            product (dict): A product dictionary.

        Returns:
            bool: True if the product matches the style preferences, False otherwise.
        """
        if not self.user_style_preferences:
            return True  # Consider it a style match if no user preferences provided. Can be configured to return false.

        if 'style' in product:
          for preference in self.user_style_preferences:
            if preference.lower() in product['style'].lower():
              return True
          return False # None of the preferences matched.
        else:
          return True # If the product doesn't specify style, consider it a match

if __name__ == '__main__':
    # Example Usage:
    custom_fit = CustomFit()

    # Set user measurements
    custom_fit.set_user_measurements({"chest": 38, "waist": 32, "hips": 40})

    # Set user style preferences
    custom_fit.set_user_style_preferences(["casual", "modern"])

    # Add products to the catalog
    custom_fit.add_product({
        "name": "T-Shirt",
        "chest_size": 38,
        "style": "casual",
        "description": "A comfortable cotton t-shirt."
    })
    custom_fit.add_product({
        "name": "Jeans",
        "waist_size": 32,
        "style": "modern",
        "description": "Slim-fit jeans."
    })
    custom_fit.add_product({
        "name": "Bohemian Dress",
        "chest_size": 36,
        "style": "bohemian",
        "description": "Flowy bohemian dress."
    })
    custom_fit.add_product({
        "name": "Oversized Coat",
        "chest_size": 40,
        "style": "casual",
        "description": "Warm and stylish coat."
    })

    # Recommend items
    recommendations = custom_fit.recommend_items()

    # Print recommendations
    if recommendations:
        print("Recommended items:")
        for item in recommendations:
            print(f"- {item['name']} ({item['style']}): {item['description']}")
    else:
        print("No items found that match your measurements and style preferences.")