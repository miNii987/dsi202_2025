from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import ClothingItem
import json
from django.db.models import Q

# Color compatibility rules (simplified)
COLOR_MATCHES = {
    "blue": ["black", "white", "navy", "grey"],
    "black": ["blue", "white", "grey"],
    "white": ["blue", "black", "navy"],
    "navy": ["white", "blue", "grey"],
    "grey": ["blue", "black", "navy"]
}

def home_view(request):
    """
    View to render the homepage
    """
    return render(request, 'home.html')

def clothing_list_view(request):
    """
    View to display a list of all clothing items with optional search
    """
    query = request.GET.get('q', '')
    clothing_items = ClothingItem.objects.all()
    if query:
        clothing_items = clothing_items.filter(
            Q(item_type__icontains=query) |
            Q(color__icontains=query) |
            Q(style__icontains=query)
        )
    return render(request, 'list.html', {
        'clothing_items': clothing_items,
        'query': query
    })

def clothing_detail_view(request, item_id):
    """
    View to display details of a specific clothing item
    """
    item = get_object_or_404(ClothingItem, id=item_id)
    return render(request, 'detail.html', {'item': item})

def outfit_matcher_view(request):
    """
    View to handle outfit matching requests.
    GET: Renders the outfit matcher template
    POST: Processes multiple clothing selections (up to 3 per type: top, bottom, dress) and generates outfit combinations
    with Top + Bottom or standalone Dress, excluding same-type matches.
    """
    if request.method == "GET":
        clothing_items = ClothingItem.objects.all()
        return render(request, 'outfit_matcher.html', {
            'clothing_items': clothing_items
        })
    
    elif request.method == "POST":
        try:
            # Get selected clothing items from POST data
            selected_items_data = request.POST.get('selected_items')
            selected_item_ids = json.loads(selected_items_data) if selected_items_data else []
            
            # Find selected items
            selected_items = ClothingItem.objects.filter(id__in=selected_item_ids)
            if not selected_items:
                return render(request, 'outfit_matcher.html', {
                    'clothing_items': ClothingItem.objects.all(),
                    'error': 'No items selected'
                })
            
            # Map item types (e.g., shirt -> top, pants -> bottom)
            for item in selected_items:
                if item.item_type.lower() in ['shirt', 'blouse', 't-shirt']:
                    item.item_type = 'top'
                elif item.item_type.lower() in ['pants', 'skirt', 'trousers']:
                    item.item_type = 'bottom'
            
            # Separate tops, bottoms, and dresses
            tops = selected_items.filter(item_type__iexact='top')
            bottoms = selected_items.filter(item_type__iexact='bottom')
            dresses = selected_items.filter(item_type__iexact='dress')
            
            # Validate selection counts
            if tops.count() > 3 or bottoms.count() > 3 or dresses.count() > 3:
                return render(request, 'outfit_matcher.html', {
                    'clothing_items': ClothingItem.objects.all(),
                    'error': 'Cannot select more than 3 items of each type'
                })
            
            # Generate outfit combinations
            outfits = []
            # Top + Bottom combinations when both are selected
            if tops and bottoms:
                for top in tops:
                    for bottom in bottoms:
                        if (top.color in COLOR_MATCHES.get(bottom.color, []) or 
                            bottom.color in COLOR_MATCHES.get(top.color, [])) and \
                            top.style == bottom.style:
                            outfits.append({
                                'top': top,
                                'bottom': bottom,
                                'dress': None
                            })
            # Standalone tops if only tops selected
            elif tops and not bottoms and not dresses:
                for top in tops:
                    outfits.append({
                        'top': top,
                        'bottom': None,
                        'dress': None
                    })
            # Standalone bottoms if only bottoms selected
            elif bottoms and not tops and not dresses:
                for bottom in bottoms:
                    outfits.append({
                        'top': None,
                        'bottom': bottom,
                        'dress': None
                    })
            # Dress as standalone
            for dress in dresses:
                outfits.append({
                    'top': None,
                    'bottom': None,
                    'dress': dress
                })
            
            if not outfits:
                return render(request, 'outfit_matcher.html', {
                    'clothing_items': ClothingItem.objects.all(),
                    'error': 'No matching outfits found for the selected items'
                })
            
            return render(request, 'outfit_matcher.html', {
                'clothing_items': ClothingItem.objects.all(),
                'outfits': outfits
            })
        
        except json.JSONDecodeError:
            return render(request, 'outfit_matcher.html', {
                'clothing_items': ClothingItem.objects.all(),
                'error': 'Invalid data format'
            })
        except Exception as e:
            return render(request, 'outfit_matcher.html', {
                'clothing_items': ClothingItem.objects.all(),
                'error': str(e)
            })