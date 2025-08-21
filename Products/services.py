from Products.models import Product


def get_products_based_on_query_params(query_params : dict):
    return (
        Product.objects.all()
        .filter_by_category(query_params.get("category"))
        .filter_by_availability("is_available" in query_params)
        .sort_by_price(query_params.get("price"))
        .most_viewed("most_view" in query_params)
        .most_purchased("most_purchase" in query_params)
    )

     