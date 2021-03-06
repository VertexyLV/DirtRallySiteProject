from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q   # library for filtering query sets.

from .models import EventInfo, LeaderBoard, TotalUniqueDrivers, TotalQualifiedDrivers, PlayersInfo,\
TotalQualifiedCountries, CountriesInfo





"""------------------------------------------------FUNCTIONS------------------------------------------------"""
# START of the code for getting integer value of total unique drivers on all leaderboard events.
def total_unique_drivers():
    total_unique_drivers_obj = TotalUniqueDrivers.objects.all()

    total_unique_drivers = 0
    for i in total_unique_drivers_obj:
        total_unique_drivers = i.player_id_list_len
    return total_unique_drivers
# END of the code for getting integer value of total unique drivers on all leaderboard events.


# START of the code for getting integer value of TotalQualifiedDrivers to templates.
def total_qualified_drivers(event_category):

    if event_category == 'overall':
        total_qualified_drivers_count = PlayersInfo.objects.all().count()
        return total_qualified_drivers_count
    elif event_category == 'daily':
        total_qualified_drivers_count = PlayersInfo.objects.filter(~Q(daily_events_finished=0)).count()
        return total_qualified_drivers_count
    elif event_category == 'daily2':
        total_qualified_drivers_count = PlayersInfo.objects.filter(~Q(daily2_events_finished=0)).count()
        return total_qualified_drivers_count
    elif event_category == 'weekly':
        total_qualified_drivers_count = PlayersInfo.objects.filter(~Q(weekly_events_finished=0)).count()
        return total_qualified_drivers_count
    elif event_category == 'weekly2':
        total_qualified_drivers_count = PlayersInfo.objects.filter(~Q(weekly2_events_finished=0)).count()
        return total_qualified_drivers_count
    elif event_category == 'monthly':
        total_qualified_drivers_count = PlayersInfo.objects.filter(~Q(monthly_events_finished=0)).count()
        return total_qualified_drivers_count
# END of the code for getting integer value of TotalQualifiedDrivers to templates.


# START of the code for getting integer value of TotalQualifiedCountries to templates.
def total_qualified_countries(event_category):

    if event_category == 'overall':
        total_qualified_countries_count = CountriesInfo.objects.all().count()
        return total_qualified_countries_count
    elif event_category == 'daily':
        total_qualified_countries_count = CountriesInfo.objects.filter(~Q(daily_events_finished=0)).count()
        return total_qualified_countries_count
    elif event_category == 'daily2':
        total_qualified_countries_count = CountriesInfo.objects.filter(~Q(daily2_events_finished=0)).count()
        return total_qualified_countries_count
    elif event_category == 'weekly':
        total_qualified_countries_count = CountriesInfo.objects.filter(~Q(weekly_events_finished=0)).count()
        return total_qualified_countries_count
    elif event_category == 'weekly2':
        total_qualified_countries_count = CountriesInfo.objects.filter(~Q(weekly2_events_finished=0)).count()
        return total_qualified_countries_count
    elif event_category == 'monthly':
        total_qualified_countries_count = CountriesInfo.objects.filter(~Q(monthly_events_finished=0)).count()
        return total_qualified_countries_count
# END of the code for getting integer value of TotalQualifiedCountries to templates.


# START of the code for getting most participants ever and in what event.
def most_participants_ever():
    most_participants_ever_obj = EventInfo.objects.order_by('-total_drivers')

    most_participants_ever_list = []
    for i in most_participants_ever_obj:
        most_participants_ever_value = i.total_drivers
        most_participants_ever_event = i.event_category
        most_participants_ever_date = i.date
        most_participants_ever_list.append(most_participants_ever_value)
        most_participants_ever_list.append(most_participants_ever_event)
        most_participants_ever_list.append(most_participants_ever_date)

        return most_participants_ever_list
# END of the code for getting most participants ever and in what event.


# START pagination function.
def pagination(request, object):

    page = request.GET.get('page', 1)

    paginator = Paginator(object, 100)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return users
# END pagination function.


# START functions for converting drivers time from seconds to time string h m s.
def time_h_m_s_converter(input_time):
    hours = 0
    minutes = 0

    if input_time < 3600:
        minutes = input_time // 60
        seconds = input_time % 60

    elif input_time < 60:
        seconds = input_time

    else:
        hours = input_time // 3600
        remainder = input_time % 3600
        if remainder < 60:
            seconds = remainder
        else:
            minutes = remainder // 60
            seconds = remainder % 60

    time_format = str(int(hours)) + 'h ' + str(int(minutes)) + 'm ' + '{0:.3f}'.format(
        round(seconds, 3)) + 's'

    return time_format
# END functions for converting drivers time from seconds to time string h m s.


# START function for events date selector string cleaning.
def date_selector_cleaner(obj, obj_type):
    unclean_date_list = []
    for i in obj:
        if obj_type == "EventInfo":
            unclean_date_list.append(i.date)
        elif obj_type == "LeaderBoard":
            unclean_date_list.append(i.event_info.date)

    split_datelist = []
    for i in unclean_date_list:
        split_datelist.append(i.split('.'))

    change_year_position_list = []
    for i in split_datelist:
        i[0], i[1], i[2] = i[2], i[0], i[1]
        change_year_position_list.append(i)

    change_year_position_list.sort()

    ordered_list_of_lists = []
    for i in change_year_position_list:
        i[2], i[0], i[1] = i[0], i[1], i[2]
        ordered_list_of_lists.append(i)

    ordered_date_list = []
    for i in ordered_list_of_lists:
        ordered_date_list.append('.'.join(i))

    return ordered_date_list[::-1]
# END function for events date selector string cleaning.
"""------------------------------------------------FUNCTIONS------------------------------------------------"""












"""------------------------------------------------TOP DRIVERS VIEW------------------------------------------------"""
def top_drivers_order_by_view(request, event_category, order_variable):


    overall_leaderboards_active_switch_button = 'leaderboards_inactive_category_switch_button'
    daily_leaderboards_active_switch_button = 'leaderboards_inactive_category_switch_button'
    daily2_leaderboards_active_switch_button = 'leaderboards_inactive_category_switch_button'
    weekly_leaderboards_active_switch_button = 'leaderboards_inactive_category_switch_button'
    weekly2_leaderboards_active_switch_button = 'leaderboards_inactive_category_switch_button'
    monthly_leaderboards_active_switch_button = 'leaderboards_inactive_category_switch_button'

    if event_category == 'overall':
        overall_leaderboards_active_switch_button = 'leaderboards_active_category_switch_button'
    elif event_category == 'daily':
        daily_leaderboards_active_switch_button = 'leaderboards_active_category_switch_button'
    elif event_category == 'daily2':
        daily2_leaderboards_active_switch_button = 'leaderboards_active_category_switch_button'
    elif event_category == 'weekly':
        weekly_leaderboards_active_switch_button = 'leaderboards_active_category_switch_button'
    elif event_category == 'weekly2':
        weekly2_leaderboards_active_switch_button = 'leaderboards_active_category_switch_button'
    elif event_category == 'monthly':
        monthly_leaderboards_active_switch_button = 'leaderboards_active_category_switch_button'

    leaderboards_th2_activity_tag = 'leaderboards_inactive_sort_button'
    leaderboards_th5_activity_tag = 'leaderboards_inactive_sort_button'
    leaderboards_th6_activity_tag = 'leaderboards_inactive_sort_button'
    leaderboards_th7_activity_tag = 'leaderboards_inactive_sort_button'
    leaderboards_th8_activity_tag = 'leaderboards_inactive_sort_button'
    leaderboards_th9_activity_tag = 'leaderboards_inactive_sort_button'
    leaderboards_th10_activity_tag = 'leaderboards_inactive_sort_button'
    leaderboards_th11_activity_tag = 'leaderboards_inactive_sort_button'
    leaderboards_th12_activity_tag = 'leaderboards_inactive_sort_button'


    # Changes filter field name and filters out all drivers with 0 events in that category.
    kwargs = {
        '{0}_{1}'.format(event_category, 'events_finished'): 0,
    }

    if order_variable == 'country_from':
        object_ordered = PlayersInfo.objects.filter(~Q(**kwargs)).order_by(order_variable,
                                                                           event_category + '_average_finish_place')
        leaderboards_th2_activity_tag = 'leaderboards_active_sort_button'

    elif order_variable == event_category + '_events_finished':
        object_ordered = PlayersInfo.objects.filter(~Q(**kwargs)).order_by('-' + order_variable,
                                                                           event_category + '_average_finish_place')
        leaderboards_th5_activity_tag = 'leaderboards_active_sort_button'

    elif order_variable == event_category + '_points':
        object_ordered = PlayersInfo.objects.filter(~Q(**kwargs)).order_by('-' + order_variable,
                                                                           event_category + '_average_finish_place')
        leaderboards_th6_activity_tag = 'leaderboards_active_sort_button'

    elif order_variable == event_category + '_average_finish_place':
        object_ordered = PlayersInfo.objects.filter(~Q(**kwargs)).order_by(order_variable,
                                                                           event_category + '_points')
        leaderboards_th7_activity_tag = 'leaderboards_active_sort_button'

    elif order_variable == event_category + '_first_places':
        object_ordered = PlayersInfo.objects.filter(~Q(**kwargs)).order_by('-' + order_variable,
                                                                           '-' + event_category + '_top_3',
                                                                           '-' + event_category + '_top_10',
                                                                           '-' + event_category + '_top_100',
                                                                           event_category + '_average_finish_place')
        leaderboards_th8_activity_tag = 'leaderboards_active_sort_button'

    elif order_variable == event_category + '_top_3':
        object_ordered = PlayersInfo.objects.filter(~Q(**kwargs)).order_by('-' + order_variable,
                                                                           '-' + event_category + '_first_places',
                                                                           '-' + event_category + '_top_10',
                                                                           '-' + event_category + '_top_100',
                                                                           event_category + '_average_finish_place')
        leaderboards_th9_activity_tag = 'leaderboards_active_sort_button'

    elif order_variable == event_category + '_top_10':
        object_ordered = PlayersInfo.objects.filter(~Q(**kwargs)).order_by('-' + order_variable,
                                                                           '-' + event_category + '_first_places',
                                                                           '-' + event_category + '_top_3',
                                                                           '-' + event_category + '_top_100',
                                                                           event_category + '_average_finish_place')
        leaderboards_th10_activity_tag = 'leaderboards_active_sort_button'

    elif order_variable == event_category + '_top_100':
        object_ordered = PlayersInfo.objects.filter(~Q(**kwargs)).order_by('-' + order_variable,
                                                                           '-' + event_category + '_first_places',
                                                                           '-' + event_category + '_top_3',
                                                                           '-' + event_category + '_top_10',
                                                                           event_category + '_average_finish_place')
        leaderboards_th11_activity_tag = 'leaderboards_active_sort_button'

    elif order_variable == event_category + '_driving_time_seconds':
        object_ordered = PlayersInfo.objects.filter(~Q(**kwargs)).order_by('-' + order_variable,
                                                                           event_category + '_average_finish_place')
        leaderboards_th12_activity_tag = 'leaderboards_active_sort_button'




    drivers = pagination(request, object_ordered)


    context = {}

    context['drivers'] = drivers
    context['event_category'] = event_category

    context['overall_qualified_drivers'] = total_qualified_drivers(event_category)
    context['daily_qualified_drivers'] = total_qualified_drivers(event_category)
    context['daily2_qualified_drivers'] = total_qualified_drivers(event_category)
    context['weekly_qualified_drivers'] = total_qualified_drivers(event_category)
    context['weekly2_qualified_drivers'] = total_qualified_drivers(event_category)
    context['monthly_qualified_drivers'] = total_qualified_drivers(event_category)

    context['overall_leaderboards_active_switch_button'] = overall_leaderboards_active_switch_button
    context['daily_leaderboards_active_switch_button'] = daily_leaderboards_active_switch_button
    context['daily2_leaderboards_active_switch_button'] = daily2_leaderboards_active_switch_button
    context['weekly_leaderboards_active_switch_button'] = weekly_leaderboards_active_switch_button
    context['weekly2_leaderboards_active_switch_button'] = weekly2_leaderboards_active_switch_button
    context['monthly_leaderboards_active_switch_button'] = monthly_leaderboards_active_switch_button

    context['leaderboards_th2_activity_tag'] = leaderboards_th2_activity_tag
    context['leaderboards_th5_activity_tag'] = leaderboards_th5_activity_tag
    context['leaderboards_th6_activity_tag'] = leaderboards_th6_activity_tag
    context['leaderboards_th7_activity_tag'] = leaderboards_th7_activity_tag
    context['leaderboards_th8_activity_tag'] = leaderboards_th8_activity_tag
    context['leaderboards_th9_activity_tag'] = leaderboards_th9_activity_tag
    context['leaderboards_th10_activity_tag'] = leaderboards_th10_activity_tag
    context['leaderboards_th11_activity_tag'] = leaderboards_th11_activity_tag
    context['leaderboards_th12_activity_tag'] = leaderboards_th12_activity_tag


    context['main_nav_button_1_tag'] = 'main_button_active'
    context['main_nav_button_2_tag'] = 'main_button_inactive'
    context['main_nav_button_3_tag'] = 'main_button_inactive'
    context['main_nav_button_4_tag'] = 'main_button_inactive'

    return render(request, 'top_drivers.html', context)
"""------------------------------------------------TOP DRIVERS VIEW------------------------------------------------"""













"""------------------------------------------------TOP COUNTRIES VIEW------------------------------------------------"""
def top_countries_order_by_view(request, event_category, order_variable):


    overall_leaderboards_active_switch_button = 'leaderboards_inactive_category_switch_button'
    daily_leaderboards_active_switch_button = 'leaderboards_inactive_category_switch_button'
    daily2_leaderboards_active_switch_button = 'leaderboards_inactive_category_switch_button'
    weekly_leaderboards_active_switch_button = 'leaderboards_inactive_category_switch_button'
    weekly2_leaderboards_active_switch_button = 'leaderboards_inactive_category_switch_button'
    monthly_leaderboards_active_switch_button = 'leaderboards_inactive_category_switch_button'

    if event_category == 'overall':
        overall_leaderboards_active_switch_button = 'leaderboards_active_category_switch_button'
    elif event_category == 'daily':
        daily_leaderboards_active_switch_button = 'leaderboards_active_category_switch_button'
    elif event_category == 'daily2':
        daily2_leaderboards_active_switch_button = 'leaderboards_active_category_switch_button'
    elif event_category == 'weekly':
        weekly_leaderboards_active_switch_button = 'leaderboards_active_category_switch_button'
    elif event_category == 'weekly2':
        weekly2_leaderboards_active_switch_button = 'leaderboards_active_category_switch_button'
    elif event_category == 'monthly':
        monthly_leaderboards_active_switch_button = 'leaderboards_active_category_switch_button'

    leaderboards_th3_activity_tag = 'leaderboards_inactive_sort_button'
    leaderboards_th4_activity_tag = 'leaderboards_inactive_sort_button'
    leaderboards_th5_activity_tag = 'leaderboards_inactive_sort_button'
    leaderboards_th6_activity_tag = 'leaderboards_inactive_sort_button'
    leaderboards_th7_activity_tag = 'leaderboards_inactive_sort_button'
    leaderboards_th8_activity_tag = 'leaderboards_inactive_sort_button'
    leaderboards_th9_activity_tag = 'leaderboards_inactive_sort_button'
    leaderboards_th10_activity_tag = 'leaderboards_inactive_sort_button'
    leaderboards_th11_activity_tag = 'leaderboards_inactive_sort_button'
    leaderboards_th12_activity_tag = 'leaderboards_inactive_sort_button'
    leaderboards_th13_activity_tag = 'leaderboards_inactive_sort_button'


    # Changes filter field name and filters out all drivers with 0 events in that category.
    kwargs = {
        '{0}_{1}'.format(event_category, 'events_finished'): 0,
    }

    if order_variable == 'country_name':
        object_ordered = CountriesInfo.objects.filter(~Q(**kwargs)).order_by(order_variable)
        leaderboards_th3_activity_tag = 'leaderboards_active_sort_button'

    elif order_variable == event_category + '_number_of_drivers':
        object_ordered = CountriesInfo.objects.filter(~Q(**kwargs)).order_by('-' + order_variable)
        leaderboards_th4_activity_tag = 'leaderboards_active_sort_button'

    elif order_variable == event_category + '_events_finished':
        object_ordered = CountriesInfo.objects.filter(~Q(**kwargs)).order_by('-' + order_variable)
        leaderboards_th5_activity_tag = 'leaderboards_active_sort_button'

    elif order_variable == event_category + '_points':
        object_ordered = CountriesInfo.objects.filter(~Q(**kwargs)).order_by('-' + order_variable)
        leaderboards_th6_activity_tag = 'leaderboards_active_sort_button'

    elif order_variable == event_category + '_average_points':
        object_ordered = CountriesInfo.objects.filter(~Q(**kwargs)).order_by('-' + order_variable)
        leaderboards_th7_activity_tag = 'leaderboards_active_sort_button'

    elif order_variable == event_category + '_average_finish_place':
        object_ordered = CountriesInfo.objects.filter(~Q(**kwargs)).order_by(order_variable)
        leaderboards_th8_activity_tag = 'leaderboards_active_sort_button'

    elif order_variable == event_category + '_first_places':
        object_ordered = CountriesInfo.objects.filter(~Q(**kwargs)).order_by('-' + order_variable, '-' + event_category + '_top_3')
        leaderboards_th9_activity_tag = 'leaderboards_active_sort_button'

    elif order_variable == event_category + '_top_3':
        object_ordered = CountriesInfo.objects.filter(~Q(**kwargs)).order_by('-' + order_variable, '-' + event_category + '_top_10')
        leaderboards_th10_activity_tag = 'leaderboards_active_sort_button'

    elif order_variable == event_category + '_top_10':
        object_ordered = CountriesInfo.objects.filter(~Q(**kwargs)).order_by('-' + order_variable, '-' + event_category + '_top_100')
        leaderboards_th11_activity_tag = 'leaderboards_active_sort_button'

    elif order_variable == event_category + '_top_100':
        object_ordered = CountriesInfo.objects.filter(~Q(**kwargs)).order_by('-' + order_variable, event_category + '_average_finish_place')
        leaderboards_th12_activity_tag = 'leaderboards_active_sort_button'

    elif order_variable == event_category + '_driving_time_seconds':
        object_ordered = CountriesInfo.objects.filter(~Q(**kwargs)).order_by('-' + order_variable)
        leaderboards_th13_activity_tag = 'leaderboards_active_sort_button'


    context = {}

    context['object_ordered'] = object_ordered
    context['event_category'] = event_category

    context['overall_qualified_countries'] = total_qualified_countries(event_category)
    context['daily_qualified_countries'] = total_qualified_countries(event_category)
    context['daily2_qualified_countries'] = total_qualified_countries(event_category)
    context['weekly_qualified_countries'] = total_qualified_countries(event_category)
    context['weekly2_qualified_countries'] = total_qualified_countries(event_category)
    context['monthly_qualified_countries'] = total_qualified_countries(event_category)

    context['overall_leaderboards_active_switch_button'] = overall_leaderboards_active_switch_button
    context['daily_leaderboards_active_switch_button'] = daily_leaderboards_active_switch_button
    context['daily2_leaderboards_active_switch_button'] = daily2_leaderboards_active_switch_button
    context['weekly_leaderboards_active_switch_button'] = weekly_leaderboards_active_switch_button
    context['weekly2_leaderboards_active_switch_button'] = weekly2_leaderboards_active_switch_button
    context['monthly_leaderboards_active_switch_button'] = monthly_leaderboards_active_switch_button

    context['leaderboards_th3_activity_tag'] = leaderboards_th3_activity_tag
    context['leaderboards_th4_activity_tag'] = leaderboards_th4_activity_tag
    context['leaderboards_th5_activity_tag'] = leaderboards_th5_activity_tag
    context['leaderboards_th6_activity_tag'] = leaderboards_th6_activity_tag
    context['leaderboards_th7_activity_tag'] = leaderboards_th7_activity_tag
    context['leaderboards_th8_activity_tag'] = leaderboards_th8_activity_tag
    context['leaderboards_th9_activity_tag'] = leaderboards_th9_activity_tag
    context['leaderboards_th10_activity_tag'] = leaderboards_th10_activity_tag
    context['leaderboards_th11_activity_tag'] = leaderboards_th11_activity_tag
    context['leaderboards_th12_activity_tag'] = leaderboards_th12_activity_tag
    context['leaderboards_th13_activity_tag'] = leaderboards_th13_activity_tag

    context['main_nav_button_1_tag'] = 'main_button_active'
    context['main_nav_button_2_tag'] = 'main_button_inactive'
    context['main_nav_button_3_tag'] = 'main_button_inactive'
    context['main_nav_button_4_tag'] = 'main_button_inactive'

    return render(request, 'top_countries.html', context)
"""------------------------------------------------TOP COUNTRIES VIEW------------------------------------------------"""











"""------------------------------------------------DRIVER STATS VIEW------------------------------------------------"""
def driverstats_view(request, drivers_id):

    name_id = 0
    try:
        if isinstance(drivers_id, int):
            name_id = 1
    except:
        pass


    if drivers_id == 'notfound':

        context = {}

        context['main_nav_button_1_tag'] = 'main_button_inactive'
        context['main_nav_button_2_tag'] = 'main_button_active'
        context['main_nav_button_3_tag'] = 'main_button_inactive'
        context['main_nav_button_4_tag'] = 'main_button_inactive'

        return render(request, 'driver_does_not_exist.html', context)

    try:
        if not LeaderBoard.objects.filter(player_id__exact=drivers_id).exists() and not LeaderBoard.objects.filter(name__exact=drivers_id).exists():

            context = {}

            context['main_nav_button_1_tag'] = 'main_button_inactive'
            context['main_nav_button_2_tag'] = 'main_button_active'
            context['main_nav_button_3_tag'] = 'main_button_inactive'
            context['main_nav_button_4_tag'] = 'main_button_inactive'

            return render(request, 'driver_does_not_exist.html', context)

    except:
        if not LeaderBoard.objects.filter(name__exact=drivers_id).exists():

            context = {}

            context['main_nav_button_1_tag'] = 'main_button_inactive'
            context['main_nav_button_2_tag'] = 'main_button_active'
            context['main_nav_button_3_tag'] = 'main_button_inactive'
            context['main_nav_button_4_tag'] = 'main_button_inactive'

            return render(request, 'driver_does_not_exist.html', context)

    playersInfo_exists = 0
    try:
        if PlayersInfo.objects.filter(player_id__exact=drivers_id).exists():

            object_playerinfo = PlayersInfo.objects.filter(player_id__exact=drivers_id)

            daily_completed_obj = LeaderBoard.objects.filter(player_id__exact=drivers_id, event_info__event_category__exact='Daily')
            daily2_completed_obj = LeaderBoard.objects.filter(player_id__exact=drivers_id, event_info__event_category__exact='Daily2')
            weekly_completed_obj = LeaderBoard.objects.filter(player_id__exact=drivers_id, event_info__event_category__exact='Weekly')
            weekly2_completed_obj = LeaderBoard.objects.filter(player_id__exact=drivers_id, event_info__event_category__exact='Weekly2')
            monthly_completed_obj = LeaderBoard.objects.filter(player_id__exact=drivers_id, event_info__event_category__exact='Monthly')

            playersInfo_exists = 1
        if playersInfo_exists == 0:
            raise()

    except:
        if PlayersInfo.objects.filter(name__exact=drivers_id).exists():

            object_playerinfo = PlayersInfo.objects.filter(name__exact=drivers_id)

            daily_completed_obj = LeaderBoard.objects.filter(name__exact=drivers_id, event_info__event_category__exact='Daily')
            daily2_completed_obj = LeaderBoard.objects.filter(name__exact=drivers_id, event_info__event_category__exact='Daily2')
            weekly_completed_obj = LeaderBoard.objects.filter(name__exact=drivers_id, event_info__event_category__exact='Weekly')
            weekly2_completed_obj = LeaderBoard.objects.filter(name__exact=drivers_id, event_info__event_category__exact='Weekly2')
            monthly_completed_obj = LeaderBoard.objects.filter(name__exact=drivers_id, event_info__event_category__exact='Monthly')

            playersInfo_exists = 1

    if playersInfo_exists == 1:

        total_daily_obj = EventInfo.objects.filter(event_category__exact='Daily')
        total_daily2_obj = EventInfo.objects.filter(event_category__exact='Daily2')
        total_weekly_obj = EventInfo.objects.filter(event_category__exact='Weekly')
        total_weekly2_obj = EventInfo.objects.filter(event_category__exact='Weekly2')
        total_monthly_obj = EventInfo.objects.filter(event_category__exact='Monthly')


        country_from = ''
        drivers_name = ''
        drivers_id = ''


        overall_events_finished = ''
        overall_points = ''
        overall_average_points = ''
        overall_average_finish_place = ''
        overall_first_places = ''
        overall_top_3 = ''
        overall_top_10 = ''
        overall_top_100 = ''
        overall_driving_time_seconds = ''

        overall_world_rank_events_finished = ''
        overall_world_rank_points = ''
        overall_world_rank_average_points = ''
        overall_world_rank_average_finish_place = ''
        overall_world_rank_first_places = ''
        overall_world_rank_top_3 = ''
        overall_world_rank_top_10 = ''
        overall_world_rank_top_100 = ''
        overall_world_rank_driving_time_seconds = ''

        overall_country_rank_events_finished = ''
        overall_country_rank_points = ''
        overall_country_rank_average_points = ''
        overall_country_rank_average_finish_place = ''
        overall_country_rank_first_places = ''
        overall_country_rank_top_3 = ''
        overall_country_rank_top_10 = ''
        overall_country_rank_top_100 = ''
        overall_country_rank_driving_time_seconds = ''


        daily_events_finished = ''
        daily_points = ''
        daily_average_points = ''
        daily_average_finish_place = ''
        daily_first_places = ''
        daily_top_3 = ''
        daily_top_10 = ''
        daily_top_100 = ''
        daily_driving_time_seconds = ''

        daily_world_rank_events_finished = ''
        daily_world_rank_points = ''
        daily_world_rank_average_points = ''
        daily_world_rank_average_finish_place = ''
        daily_world_rank_first_places = ''
        daily_world_rank_top_3 = ''
        daily_world_rank_top_10 = ''
        daily_world_rank_top_100 = ''
        daily_world_rank_driving_time_seconds = ''

        daily_country_rank_events_finished = ''
        daily_country_rank_points = ''
        daily_country_rank_average_points = ''
        daily_country_rank_average_finish_place = ''
        daily_country_rank_first_places = ''
        daily_country_rank_top_3 = ''
        daily_country_rank_top_10 = ''
        daily_country_rank_top_100 = ''
        daily_country_rank_driving_time_seconds = ''


        daily2_events_finished = ''
        daily2_points = ''
        daily2_average_points = ''
        daily2_average_finish_place = ''
        daily2_first_places = ''
        daily2_top_3 = ''
        daily2_top_10 = ''
        daily2_top_100 = ''
        daily2_driving_time_seconds = ''

        daily2_world_rank_events_finished = ''
        daily2_world_rank_points = ''
        daily2_world_rank_average_points = ''
        daily2_world_rank_average_finish_place = ''
        daily2_world_rank_first_places = ''
        daily2_world_rank_top_3 = ''
        daily2_world_rank_top_10 = ''
        daily2_world_rank_top_100 = ''
        daily2_world_rank_driving_time_seconds = ''

        daily2_country_rank_events_finished = ''
        daily2_country_rank_points = ''
        daily2_country_rank_average_points = ''
        daily2_country_rank_average_finish_place = ''
        daily2_country_rank_first_places = ''
        daily2_country_rank_top_3 = ''
        daily2_country_rank_top_10 = ''
        daily2_country_rank_top_100 = ''
        daily2_country_rank_driving_time_seconds = ''


        weekly_events_finished = ''
        weekly_points = ''
        weekly_average_points = ''
        weekly_average_finish_place = ''
        weekly_first_places = ''
        weekly_top_3 = ''
        weekly_top_10 = ''
        weekly_top_100 = ''
        weekly_driving_time_seconds = ''

        weekly_world_rank_events_finished = ''
        weekly_world_rank_points = ''
        weekly_world_rank_average_points = ''
        weekly_world_rank_average_finish_place = ''
        weekly_world_rank_first_places = ''
        weekly_world_rank_top_3 = ''
        weekly_world_rank_top_10 = ''
        weekly_world_rank_top_100 = ''
        weekly_world_rank_driving_time_seconds = ''

        weekly_country_rank_events_finished = ''
        weekly_country_rank_points = ''
        weekly_country_rank_average_points = ''
        weekly_country_rank_average_finish_place = ''
        weekly_country_rank_first_places = ''
        weekly_country_rank_top_3 = ''
        weekly_country_rank_top_10 = ''
        weekly_country_rank_top_100 = ''
        weekly_country_rank_driving_time_seconds = ''


        weekly2_events_finished = ''
        weekly2_points = ''
        weekly2_average_points = ''
        weekly2_average_finish_place = ''
        weekly2_first_places = ''
        weekly2_top_3 = ''
        weekly2_top_10 = ''
        weekly2_top_100 = ''
        weekly2_driving_time_seconds = ''

        weekly2_world_rank_events_finished = ''
        weekly2_world_rank_points = ''
        weekly2_world_rank_average_points = ''
        weekly2_world_rank_average_finish_place = ''
        weekly2_world_rank_first_places = ''
        weekly2_world_rank_top_3 = ''
        weekly2_world_rank_top_10 = ''
        weekly2_world_rank_top_100 = ''
        weekly2_world_rank_driving_time_seconds = ''

        weekly2_country_rank_events_finished = ''
        weekly2_country_rank_points = ''
        weekly2_country_rank_average_points = ''
        weekly2_country_rank_average_finish_place = ''
        weekly2_country_rank_first_places = ''
        weekly2_country_rank_top_3 = ''
        weekly2_country_rank_top_10 = ''
        weekly2_country_rank_top_100 = ''
        weekly2_country_rank_driving_time_seconds = ''


        monthly_events_finished = ''
        monthly_points = ''
        monthly_average_points = ''
        monthly_average_finish_place = ''
        monthly_first_places = ''
        monthly_top_3 = ''
        monthly_top_10 = ''
        monthly_top_100 = ''
        monthly_driving_time_seconds = ''

        monthly_world_rank_events_finished = ''
        monthly_world_rank_points = ''
        monthly_world_rank_average_points = ''
        monthly_world_rank_average_finish_place = ''
        monthly_world_rank_first_places = ''
        monthly_world_rank_top_3 = ''
        monthly_world_rank_top_10 = ''
        monthly_world_rank_top_100 = ''
        monthly_world_rank_driving_time_seconds = ''

        monthly_country_rank_events_finished = ''
        monthly_country_rank_points = ''
        monthly_country_rank_average_points = ''
        monthly_country_rank_average_finish_place = ''
        monthly_country_rank_first_places = ''
        monthly_country_rank_top_3 = ''
        monthly_country_rank_top_10 = ''
        monthly_country_rank_top_100 = ''
        monthly_country_rank_driving_time_seconds = ''


        for i in object_playerinfo:
            country_from = i.country_from
            drivers_name = i.name
            drivers_id = i.player_id

            overall_events_finished = i.overall_events_finished
            overall_points = i.overall_points
            overall_average_points = round((i.overall_points / overall_events_finished), 1)
            overall_average_finish_place = i.overall_average_finish_place
            overall_first_places = i.overall_first_places
            overall_top_3 = i.overall_top_3
            overall_top_10 = i.overall_top_10
            overall_top_100 = i.overall_top_100
            overall_driving_time_seconds = i.overall_driving_time_seconds

            overall_world_rank_events_finished = i.overall_world_rank_events_finished
            overall_world_rank_points = i.overall_world_rank_points
            overall_world_rank_average_points = i.overall_world_rank_average_points
            overall_world_rank_average_finish_place = i.overall_world_rank_average_finish_place
            overall_world_rank_first_places = i.overall_world_rank_first_places
            overall_world_rank_top_3 = i.overall_world_rank_top_3
            overall_world_rank_top_10 = i.overall_world_rank_top_10
            overall_world_rank_top_100 = i.overall_world_rank_top_100
            overall_world_rank_driving_time_seconds = i.overall_world_rank_driving_time_seconds

            overall_country_rank_events_finished = i.overall_country_rank_events_finished
            overall_country_rank_points = i.overall_country_rank_points
            overall_country_rank_average_points = i.overall_country_rank_average_points
            overall_country_rank_average_finish_place = i.overall_country_rank_average_finish_place
            overall_country_rank_first_places = i.overall_country_rank_first_places
            overall_country_rank_top_3 = i.overall_country_rank_top_3
            overall_country_rank_top_10 = i.overall_country_rank_top_10
            overall_country_rank_top_100 = i.overall_country_rank_top_100
            overall_country_rank_driving_time_seconds = i.overall_country_rank_driving_time_seconds

            daily_events_finished = i.daily_events_finished
            if daily_events_finished != 0:
                daily_points = i.daily_points
                daily_average_points = round((i.daily_points / daily_events_finished), 1)
                daily_average_finish_place = i.daily_average_finish_place
                daily_first_places = i.daily_first_places
                daily_top_3 = i.daily_top_3
                daily_top_10 = i.daily_top_10
                daily_top_100 = i.daily_top_100
                daily_driving_time_seconds = i.daily_driving_time_seconds

                daily_world_rank_events_finished = i.daily_world_rank_events_finished
                daily_world_rank_points = i.daily_world_rank_points
                daily_world_rank_average_points = i.daily_world_rank_average_points
                daily_world_rank_average_finish_place = i.daily_world_rank_average_finish_place
                daily_world_rank_first_places = i.daily_world_rank_first_places
                daily_world_rank_top_3 = i.daily_world_rank_top_3
                daily_world_rank_top_10 = i.daily_world_rank_top_10
                daily_world_rank_top_100 = i.daily_world_rank_top_100
                daily_world_rank_driving_time_seconds = i.daily_world_rank_driving_time_seconds

                daily_country_rank_events_finished = i.daily_country_rank_events_finished
                daily_country_rank_points = i.daily_country_rank_points
                daily_country_rank_average_points = i.daily_country_rank_average_points
                daily_country_rank_average_finish_place = i.daily_country_rank_average_finish_place
                daily_country_rank_first_places = i.daily_country_rank_first_places
                daily_country_rank_top_3 = i.daily_country_rank_top_3
                daily_country_rank_top_10 = i.daily_country_rank_top_10
                daily_country_rank_top_100 = i.daily_country_rank_top_100
                daily_country_rank_driving_time_seconds = i.daily_country_rank_driving_time_seconds

            daily2_events_finished = i.daily2_events_finished
            if daily2_events_finished != 0:
                daily2_points = i.daily2_points
                daily2_average_points = round((i.daily2_points / daily2_events_finished), 1)
                daily2_average_finish_place = i.daily2_average_finish_place
                daily2_first_places = i.daily2_first_places
                daily2_top_3 = i.daily2_top_3
                daily2_top_10 = i.daily2_top_10
                daily2_top_100 = i.daily2_top_100
                daily2_driving_time_seconds = i.daily2_driving_time_seconds

                daily2_world_rank_events_finished = i.daily2_world_rank_events_finished
                daily2_world_rank_points = i.daily2_world_rank_points
                daily2_world_rank_average_points = i.daily2_world_rank_average_points
                daily2_world_rank_average_finish_place = i.daily2_world_rank_average_finish_place
                daily2_world_rank_first_places = i.daily2_world_rank_first_places
                daily2_world_rank_top_3 = i.daily2_world_rank_top_3
                daily2_world_rank_top_10 = i.daily2_world_rank_top_10
                daily2_world_rank_top_100 = i.daily2_world_rank_top_100
                daily2_world_rank_driving_time_seconds = i.daily2_world_rank_driving_time_seconds

                daily2_country_rank_events_finished = i.daily2_country_rank_events_finished
                daily2_country_rank_points = i.daily2_country_rank_points
                daily2_country_rank_average_points = i.daily2_country_rank_average_points
                daily2_country_rank_average_finish_place = i.daily2_country_rank_average_finish_place
                daily2_country_rank_first_places = i.daily2_country_rank_first_places
                daily2_country_rank_top_3 = i.daily2_country_rank_top_3
                daily2_country_rank_top_10 = i.daily2_country_rank_top_10
                daily2_country_rank_top_100 = i.daily2_country_rank_top_100
                daily2_country_rank_driving_time_seconds = i.daily2_country_rank_driving_time_seconds

            weekly_events_finished = i.weekly_events_finished
            if weekly_events_finished != 0:
                weekly_points = i.weekly_points
                weekly_average_points = round((i.weekly_points / weekly_events_finished), 1)
                weekly_average_finish_place = i.weekly_average_finish_place
                weekly_first_places = i.weekly_first_places
                weekly_top_3 = i.weekly_top_3
                weekly_top_10 = i.weekly_top_10
                weekly_top_100 = i.weekly_top_100
                weekly_driving_time_seconds = i.weekly_driving_time_seconds

                weekly_world_rank_events_finished = i.weekly_world_rank_events_finished
                weekly_world_rank_points = i.weekly_world_rank_points
                weekly_world_rank_average_points = i.weekly_world_rank_average_points
                weekly_world_rank_average_finish_place = i.weekly_world_rank_average_finish_place
                weekly_world_rank_first_places = i.weekly_world_rank_first_places
                weekly_world_rank_top_3 = i.weekly_world_rank_top_3
                weekly_world_rank_top_10 = i.weekly_world_rank_top_10
                weekly_world_rank_top_100 = i.weekly_world_rank_top_100
                weekly_world_rank_driving_time_seconds = i.weekly_world_rank_driving_time_seconds

                weekly_country_rank_events_finished = i.weekly_country_rank_events_finished
                weekly_country_rank_points = i.weekly_country_rank_points
                weekly_country_rank_average_points = i.weekly_country_rank_average_points
                weekly_country_rank_average_finish_place = i.weekly_country_rank_average_finish_place
                weekly_country_rank_first_places = i.weekly_country_rank_first_places
                weekly_country_rank_top_3 = i.weekly_country_rank_top_3
                weekly_country_rank_top_10 = i.weekly_country_rank_top_10
                weekly_country_rank_top_100 = i.weekly_country_rank_top_100
                weekly_country_rank_driving_time_seconds = i.weekly_country_rank_driving_time_seconds

            weekly2_events_finished = i.weekly2_events_finished
            if weekly2_events_finished != 0:
                weekly2_points = i.weekly2_points
                weekly2_average_points = round((i.weekly2_points / weekly2_events_finished), 1)
                weekly2_average_finish_place = i.weekly2_average_finish_place
                weekly2_first_places = i.weekly2_first_places
                weekly2_top_3 = i.weekly2_top_3
                weekly2_top_10 = i.weekly2_top_10
                weekly2_top_100 = i.weekly2_top_100
                weekly2_driving_time_seconds = i.weekly2_driving_time_seconds

                weekly2_world_rank_events_finished = i.weekly2_world_rank_events_finished
                weekly2_world_rank_points = i.weekly2_world_rank_points
                weekly2_world_rank_average_points = i.weekly2_world_rank_average_points
                weekly2_world_rank_average_finish_place = i.weekly2_world_rank_average_finish_place
                weekly2_world_rank_first_places = i.weekly2_world_rank_first_places
                weekly2_world_rank_top_3 = i.weekly2_world_rank_top_3
                weekly2_world_rank_top_10 = i.weekly2_world_rank_top_10
                weekly2_world_rank_top_100 = i.weekly2_world_rank_top_100
                weekly2_world_rank_driving_time_seconds = i.weekly2_world_rank_driving_time_seconds

                weekly2_country_rank_events_finished = i.weekly2_country_rank_events_finished
                weekly2_country_rank_points = i.weekly2_country_rank_points
                weekly2_country_rank_average_points = i.weekly2_country_rank_average_points
                weekly2_country_rank_average_finish_place = i.weekly2_country_rank_average_finish_place
                weekly2_country_rank_first_places = i.weekly2_country_rank_first_places
                weekly2_country_rank_top_3 = i.weekly2_country_rank_top_3
                weekly2_country_rank_top_10 = i.weekly2_country_rank_top_10
                weekly2_country_rank_top_100 = i.weekly2_country_rank_top_100
                weekly2_country_rank_driving_time_seconds = i.weekly2_country_rank_driving_time_seconds

            monthly_events_finished = i.monthly_events_finished
            if monthly_events_finished != 0:
                monthly_points = i.monthly_points
                monthly_average_points = round((i.monthly_points / monthly_events_finished), 1)
                monthly_average_finish_place = i.monthly_average_finish_place
                monthly_first_places = i.monthly_first_places
                monthly_top_3 = i.monthly_top_3
                monthly_top_10 = i.monthly_top_10
                monthly_top_100 = i.monthly_top_100
                monthly_driving_time_seconds = i.monthly_driving_time_seconds

                monthly_world_rank_events_finished = i.monthly_world_rank_events_finished
                monthly_world_rank_points = i.monthly_world_rank_points
                monthly_world_rank_average_points = i.monthly_world_rank_average_points
                monthly_world_rank_average_finish_place = i.monthly_world_rank_average_finish_place
                monthly_world_rank_first_places = i.monthly_world_rank_first_places
                monthly_world_rank_top_3 = i.monthly_world_rank_top_3
                monthly_world_rank_top_10 = i.monthly_world_rank_top_10
                monthly_world_rank_top_100 = i.monthly_world_rank_top_100
                monthly_world_rank_driving_time_seconds = i.monthly_world_rank_driving_time_seconds

                monthly_country_rank_events_finished = i.monthly_country_rank_events_finished
                monthly_country_rank_points = i.monthly_country_rank_points
                monthly_country_rank_average_points = i.monthly_country_rank_average_points
                monthly_country_rank_average_finish_place = i.monthly_country_rank_average_finish_place
                monthly_country_rank_first_places = i.monthly_country_rank_first_places
                monthly_country_rank_top_3 = i.monthly_country_rank_top_3
                monthly_country_rank_top_10 = i.monthly_country_rank_top_10
                monthly_country_rank_top_100 = i.monthly_country_rank_top_100
                monthly_country_rank_driving_time_seconds = i.monthly_country_rank_driving_time_seconds



        context = {}

        context['country_from'] = country_from
        context['drivers_name'] = drivers_name
        context['drivers_id'] = drivers_id

        context['overall_events_finished'] = overall_events_finished
        context['overall_points'] = overall_points
        context['overall_average_points'] = overall_average_points
        context['overall_average_finish_place'] = overall_average_finish_place
        context['overall_first_places'] = overall_first_places
        context['overall_top_3'] = overall_top_3
        context['overall_top_10'] = overall_top_10
        context['overall_top_100'] = overall_top_100
        context['overall_driving_time_seconds'] = overall_driving_time_seconds

        context['daily_events_finished'] = daily_events_finished
        context['daily_points'] = daily_points
        context['daily_average_points'] = daily_average_points
        context['daily_average_finish_place'] = daily_average_finish_place
        context['daily_first_places'] = daily_first_places
        context['daily_top_3'] = daily_top_3
        context['daily_top_10'] = daily_top_10
        context['daily_top_100'] = daily_top_100
        context['daily_driving_time_seconds'] = daily_driving_time_seconds

        context['daily2_events_finished'] = daily2_events_finished
        context['daily2_points'] = daily2_points
        context['daily2_average_points'] = daily2_average_points
        context['daily2_average_finish_place'] = daily2_average_finish_place
        context['daily2_first_places'] = daily2_first_places
        context['daily2_top_3'] = daily2_top_3
        context['daily2_top_10'] = daily2_top_10
        context['daily2_top_100'] = daily2_top_100
        context['daily2_driving_time_seconds'] = daily2_driving_time_seconds

        context['weekly_events_finished'] = weekly_events_finished
        context['weekly_points'] = weekly_points
        context['weekly_average_points'] = weekly_average_points
        context['weekly_average_finish_place'] = weekly_average_finish_place
        context['weekly_first_places'] = weekly_first_places
        context['weekly_top_3'] = weekly_top_3
        context['weekly_top_10'] = weekly_top_10
        context['weekly_top_100'] = weekly_top_100
        context['weekly_driving_time_seconds'] = weekly_driving_time_seconds

        context['weekly2_events_finished'] = weekly2_events_finished
        context['weekly2_points'] = weekly2_points
        context['weekly2_average_points'] = weekly2_average_points
        context['weekly2_average_finish_place'] = weekly2_average_finish_place
        context['weekly2_first_places'] = weekly2_first_places
        context['weekly2_top_3'] = weekly2_top_3
        context['weekly2_top_10'] = weekly2_top_10
        context['weekly2_top_100'] = weekly2_top_100
        context['weekly2_driving_time_seconds'] = weekly2_driving_time_seconds

        context['monthly_events_finished'] = monthly_events_finished
        context['monthly_points'] = monthly_points
        context['monthly_average_points'] = monthly_average_points
        context['monthly_average_finish_place'] = monthly_average_finish_place
        context['monthly_first_places'] = monthly_first_places
        context['monthly_top_3'] = monthly_top_3
        context['monthly_top_10'] = monthly_top_10
        context['monthly_top_100'] = monthly_top_100
        context['monthly_driving_time_seconds'] = monthly_driving_time_seconds


        context['overall_world_rank_events_finished'] = overall_world_rank_events_finished
        context['overall_world_rank_points'] = overall_world_rank_points
        context['overall_world_rank_average_points'] = overall_world_rank_average_points
        context['overall_world_rank_average_finish_place'] = overall_world_rank_average_finish_place
        context['overall_world_rank_first_places'] = overall_world_rank_first_places
        context['overall_world_rank_top_3'] = overall_world_rank_top_3
        context['overall_world_rank_top_10'] = overall_world_rank_top_10
        context['overall_world_rank_top_100'] = overall_world_rank_top_100
        context['overall_world_rank_driving_time_seconds'] = overall_world_rank_driving_time_seconds

        context['overall_country_rank_events_finished'] = overall_country_rank_events_finished
        context['overall_country_rank_points'] = overall_country_rank_points
        context['overall_country_rank_average_points'] = overall_country_rank_average_points
        context['overall_country_rank_average_finish_place'] = overall_country_rank_average_finish_place
        context['overall_country_rank_first_places'] = overall_country_rank_first_places
        context['overall_country_rank_top_3'] = overall_country_rank_top_3
        context['overall_country_rank_top_10'] = overall_country_rank_top_10
        context['overall_country_rank_top_100'] = overall_country_rank_top_100
        context['overall_country_rank_driving_time_seconds'] = overall_country_rank_driving_time_seconds


        context['daily_world_rank_events_finished'] = daily_world_rank_events_finished
        context['daily_world_rank_points'] = daily_world_rank_points
        context['daily_world_rank_average_points'] = daily_world_rank_average_points
        context['daily_world_rank_average_finish_place'] = daily_world_rank_average_finish_place
        context['daily_world_rank_first_places'] = daily_world_rank_first_places
        context['daily_world_rank_top_3'] = daily_world_rank_top_3
        context['daily_world_rank_top_10'] = daily_world_rank_top_10
        context['daily_world_rank_top_100'] = daily_world_rank_top_100
        context['daily_world_rank_driving_time_seconds'] = daily_world_rank_driving_time_seconds

        context['daily_country_rank_events_finished'] = daily_country_rank_events_finished
        context['daily_country_rank_points'] = daily_country_rank_points
        context['daily_country_rank_average_points'] = daily_country_rank_average_points
        context['daily_country_rank_average_finish_place'] = daily_country_rank_average_finish_place
        context['daily_country_rank_first_places'] = daily_country_rank_first_places
        context['daily_country_rank_top_3'] = daily_country_rank_top_3
        context['daily_country_rank_top_10'] = daily_country_rank_top_10
        context['daily_country_rank_top_100'] = daily_country_rank_top_100
        context['daily_country_rank_driving_time_seconds'] = daily_country_rank_driving_time_seconds


        context['daily2_world_rank_events_finished'] = daily2_world_rank_events_finished
        context['daily2_world_rank_points'] = daily2_world_rank_points
        context['daily2_world_rank_average_points'] = daily2_world_rank_average_points
        context['daily2_world_rank_average_finish_place'] = daily2_world_rank_average_finish_place
        context['daily2_world_rank_first_places'] = daily2_world_rank_first_places
        context['daily2_world_rank_top_3'] = daily2_world_rank_top_3
        context['daily2_world_rank_top_10'] = daily2_world_rank_top_10
        context['daily2_world_rank_top_100'] = daily2_world_rank_top_100
        context['daily2_world_rank_driving_time_seconds'] = daily2_world_rank_driving_time_seconds

        context['daily2_country_rank_events_finished'] = daily2_country_rank_events_finished
        context['daily2_country_rank_points'] = daily2_country_rank_points
        context['daily2_country_rank_average_points'] = daily2_country_rank_average_points
        context['daily2_country_rank_average_finish_place'] = daily2_country_rank_average_finish_place
        context['daily2_country_rank_first_places'] = daily2_country_rank_first_places
        context['daily2_country_rank_top_3'] = daily2_country_rank_top_3
        context['daily2_country_rank_top_10'] = daily2_country_rank_top_10
        context['daily2_country_rank_top_100'] = daily2_country_rank_top_100
        context['daily2_country_rank_driving_time_seconds'] = daily2_country_rank_driving_time_seconds


        context['weekly_world_rank_events_finished'] = weekly_world_rank_events_finished
        context['weekly_world_rank_points'] = weekly_world_rank_points
        context['weekly_world_rank_average_points'] = weekly_world_rank_average_points
        context['weekly_world_rank_average_finish_place'] = weekly_world_rank_average_finish_place
        context['weekly_world_rank_first_places'] = weekly_world_rank_first_places
        context['weekly_world_rank_top_3'] = weekly_world_rank_top_3
        context['weekly_world_rank_top_10'] = weekly_world_rank_top_10
        context['weekly_world_rank_top_100'] = weekly_world_rank_top_100
        context['weekly_world_rank_driving_time_seconds'] = weekly_world_rank_driving_time_seconds

        context['weekly_country_rank_events_finished'] = weekly_country_rank_events_finished
        context['weekly_country_rank_points'] = weekly_country_rank_points
        context['weekly_country_rank_average_points'] = weekly_country_rank_average_points
        context['weekly_country_rank_average_finish_place'] = weekly_country_rank_average_finish_place
        context['weekly_country_rank_first_places'] = weekly_country_rank_first_places
        context['weekly_country_rank_top_3'] = weekly_country_rank_top_3
        context['weekly_country_rank_top_10'] = weekly_country_rank_top_10
        context['weekly_country_rank_top_100'] = weekly_country_rank_top_100
        context['weekly_country_rank_driving_time_seconds'] = weekly_country_rank_driving_time_seconds


        context['weekly2_world_rank_events_finished'] = weekly2_world_rank_events_finished
        context['weekly2_world_rank_points'] = weekly2_world_rank_points
        context['weekly2_world_rank_average_points'] = weekly2_world_rank_average_points
        context['weekly2_world_rank_average_finish_place'] = weekly2_world_rank_average_finish_place
        context['weekly2_world_rank_first_places'] = weekly2_world_rank_first_places
        context['weekly2_world_rank_top_3'] = weekly2_world_rank_top_3
        context['weekly2_world_rank_top_10'] = weekly2_world_rank_top_10
        context['weekly2_world_rank_top_100'] = weekly2_world_rank_top_100
        context['weekly2_world_rank_driving_time_seconds'] = weekly2_world_rank_driving_time_seconds

        context['weekly2_country_rank_events_finished'] = weekly2_country_rank_events_finished
        context['weekly2_country_rank_points'] = weekly2_country_rank_points
        context['weekly2_country_rank_average_points'] = weekly2_country_rank_average_points
        context['weekly2_country_rank_average_finish_place'] = weekly2_country_rank_average_finish_place
        context['weekly2_country_rank_first_places'] = weekly2_country_rank_first_places
        context['weekly2_country_rank_top_3'] = weekly2_country_rank_top_3
        context['weekly2_country_rank_top_10'] = weekly2_country_rank_top_10
        context['weekly2_country_rank_top_100'] = weekly2_country_rank_top_100
        context['weekly2_country_rank_driving_time_seconds'] = weekly2_country_rank_driving_time_seconds


        context['monthly_world_rank_events_finished'] = monthly_world_rank_events_finished
        context['monthly_world_rank_points'] = monthly_world_rank_points
        context['monthly_world_rank_average_points'] = monthly_world_rank_average_points
        context['monthly_world_rank_average_finish_place'] = monthly_world_rank_average_finish_place
        context['monthly_world_rank_first_places'] = monthly_world_rank_first_places
        context['monthly_world_rank_top_3'] = monthly_world_rank_top_3
        context['monthly_world_rank_top_10'] = monthly_world_rank_top_10
        context['monthly_world_rank_top_100'] = monthly_world_rank_top_100
        context['monthly_world_rank_driving_time_seconds'] = monthly_world_rank_driving_time_seconds

        context['monthly_country_rank_events_finished'] = monthly_country_rank_events_finished
        context['monthly_country_rank_points'] = monthly_country_rank_points
        context['monthly_country_rank_average_points'] = monthly_country_rank_average_points
        context['monthly_country_rank_average_finish_place'] = monthly_country_rank_average_finish_place
        context['monthly_country_rank_first_places'] = monthly_country_rank_first_places
        context['monthly_country_rank_top_3'] = monthly_country_rank_top_3
        context['monthly_country_rank_top_10'] = monthly_country_rank_top_10
        context['monthly_country_rank_top_100'] = monthly_country_rank_top_100
        context['monthly_country_rank_driving_time_seconds'] = monthly_country_rank_driving_time_seconds


        context['daily_events_completed'] = len(daily_completed_obj)
        context['daily2_events_completed'] = len(daily2_completed_obj)
        context['weekly_events_completed'] = len(weekly_completed_obj)
        context['weekly2_events_completed'] = len(weekly2_completed_obj)
        context['monthly_events_completed'] = len(monthly_completed_obj)

        context['total_daily_events'] = len(total_daily_obj)
        context['total_daily2_events'] = len(total_daily2_obj)
        context['total_weekly_events'] = len(total_weekly_obj)
        context['total_weekly2_events'] = len(total_weekly2_obj)
        context['total_monthly_events'] = len(total_monthly_obj)

        if len(total_daily_obj) != 0:
            context['daily_events_completed_percent'] = round(len(daily_completed_obj) / len(total_daily_obj) * 100, 2)
        if len(total_daily2_obj) != 0:
            context['daily2_events_completed_percent'] = round(len(daily2_completed_obj) / len(total_daily2_obj) * 100, 2)
        if len(total_weekly_obj) != 0:
            context['weekly_events_completed_percent'] = round(len(weekly_completed_obj) / len(total_weekly_obj) * 100, 2)
        if len(total_weekly2_obj) != 0:
            context['weekly2_events_completed_percent'] = round(len(weekly2_completed_obj) / len(total_weekly2_obj) * 100, 2)
        if len(total_monthly_obj) != 0:
            context['monthly_events_completed_percent'] = round(len(monthly_completed_obj) / len(total_monthly_obj) * 100, 2)

        context['daily_events_date_list'] = date_selector_cleaner(daily_completed_obj, 'LeaderBoard')
        context['daily2_events_date_list'] = date_selector_cleaner(daily2_completed_obj, 'LeaderBoard')
        context['weekly_events_date_list'] = date_selector_cleaner(weekly_completed_obj, 'LeaderBoard')
        context['weekly2_events_date_list'] = date_selector_cleaner(weekly2_completed_obj, 'LeaderBoard')
        context['monthly_events_date_list'] = date_selector_cleaner(monthly_completed_obj, 'LeaderBoard')

        context['main_nav_button_1_tag'] = 'main_button_inactive'
        context['main_nav_button_2_tag'] = 'main_button_active'
        context['main_nav_button_3_tag'] = 'main_button_inactive'
        context['main_nav_button_4_tag'] = 'main_button_inactive'


        return render(request, 'driver_stats.html', context)


    # If drivers id in PlayersInfo database does not exist, use one of these two codes.
    # But it exists in LeaderBoards.
    else:
        try:
            if LeaderBoard.objects.filter(player_id__exact=drivers_id).exists():
                object_leaderboard = LeaderBoard.objects.filter(player_id__exact=drivers_id)
        except:
            object_leaderboard = LeaderBoard.objects.filter(name__exact=drivers_id)

        finished_events = 0
        for _ in object_leaderboard:
            finished_events += 1

        context = {}

        context['finished_events'] = finished_events

        context['main_nav_button_1_tag'] = 'main_button_inactive'
        context['main_nav_button_2_tag'] = 'main_button_active'
        context['main_nav_button_3_tag'] = 'main_button_inactive'
        context['main_nav_button_4_tag'] = 'main_button_inactive'

        return render(request, 'no_qualified_drivers_page.html', context)


"""------------------------------------------------DRIVER STATS VIEW------------------------------------------------"""











"""------------------------------------------------COUNTRY STATS VIEW------------------------------------------------"""
def countrystats_view(request, country_name, event_category, order_variable):

    overall_stats_active_switch_button = 'stats_inactive_category_switch_button'
    daily_stats_active_switch_button = 'stats_inactive_category_switch_button'
    daily2_stats_active_switch_button = 'stats_inactive_category_switch_button'
    weekly_stats_active_switch_button = 'stats_inactive_category_switch_button'
    weekly2_stats_active_switch_button = 'stats_inactive_category_switch_button'
    monthly_stats_active_switch_button = 'stats_inactive_category_switch_button'

    if event_category == 'overall':
        overall_stats_active_switch_button = 'stats_active_category_switch_button'
    elif event_category == 'daily':
        daily_stats_active_switch_button = 'stats_active_category_switch_button'
    elif event_category == 'daily2':
        daily2_stats_active_switch_button = 'stats_active_category_switch_button'
    elif event_category == 'weekly':
        weekly_stats_active_switch_button = 'stats_active_category_switch_button'
    elif event_category == 'weekly2':
        weekly2_stats_active_switch_button = 'stats_active_category_switch_button'
    elif event_category == 'monthly':
        monthly_stats_active_switch_button = 'stats_active_category_switch_button'


    stats_th4_activity_tag = 'stats_inactive_sort_button'
    stats_th5_activity_tag = 'stats_inactive_sort_button'
    stats_th6_activity_tag = 'stats_inactive_sort_button'
    stats_th7_activity_tag = 'stats_inactive_sort_button'
    stats_th8_activity_tag = 'stats_inactive_sort_button'
    stats_th9_activity_tag = 'stats_inactive_sort_button'
    stats_th10_activity_tag = 'stats_inactive_sort_button'
    stats_th11_activity_tag = 'stats_inactive_sort_button'


    # Changes filter field name and filters out all drivers with 0 events in that category.
    kwargs = {
        '{0}_{1}'.format(event_category, 'events_finished'): 0,
    }

    if order_variable == event_category + '_events_finished':
        object_ordered = PlayersInfo.objects.filter(country_from__exact=country_name).filter(~Q(**kwargs)).order_by('-' + order_variable, event_category + '_average_finish_place')
        stats_th4_activity_tag = 'stats_active_sort_button'

    elif order_variable == event_category + '_points':
        object_ordered = PlayersInfo.objects.filter(country_from__exact=country_name).filter(~Q(**kwargs)).order_by('-' + order_variable, event_category + '_average_finish_place')
        stats_th5_activity_tag = 'stats_active_sort_button'

    elif order_variable == event_category + '_average_finish_place':
        object_ordered = PlayersInfo.objects.filter(country_from__exact=country_name).filter(~Q(**kwargs)).order_by(order_variable, event_category + '_points')
        stats_th6_activity_tag = 'stats_active_sort_button'

    elif order_variable == event_category + '_first_places':
        object_ordered = PlayersInfo.objects.filter(country_from__exact=country_name).filter(~Q(**kwargs)).order_by('-' + order_variable,
                                                                                                                    '-' + event_category + '_top_3',
                                                                                                                    '-' + event_category + '_top_10',
                                                                                                                    '-' + event_category + '_top_100',
                                                                                                                    event_category + '_average_finish_place')
        stats_th7_activity_tag = 'stats_active_sort_button'

    elif order_variable == event_category + '_top_3':
        object_ordered = PlayersInfo.objects.filter(country_from__exact=country_name).filter(~Q(**kwargs)).order_by('-' + order_variable,
                                                                                                                    '-' + event_category + '_first_places',
                                                                                                                    '-' + event_category + '_top_10',
                                                                                                                    '-' + event_category + '_top_100',
                                                                                                                    event_category + '_average_finish_place')
        stats_th8_activity_tag = 'stats_active_sort_button'

    elif order_variable == event_category + '_top_10':
        object_ordered = PlayersInfo.objects.filter(country_from__exact=country_name).filter(~Q(**kwargs)).order_by('-' + order_variable,
                                                                                                                    '-' + event_category + '_first_places',
                                                                                                                    '-' + event_category + '_top_3',
                                                                                                                    '-' + event_category + '_top_100',
                                                                                                                    event_category + '_average_finish_place')
        stats_th9_activity_tag = 'stats_active_sort_button'

    elif order_variable == event_category + '_top_100':
        object_ordered = PlayersInfo.objects.filter(country_from__exact=country_name).filter(~Q(**kwargs)).order_by('-' + order_variable,
                                                                                                                    '-' + event_category + '_first_places',
                                                                                                                    '-' + event_category + '_top_3',
                                                                                                                    '-' + event_category + '_top_10',
                                                                                                                    event_category + '_average_finish_place')
        stats_th10_activity_tag = 'stats_active_sort_button'

    elif order_variable == event_category + '_driving_time_seconds':
        object_ordered = PlayersInfo.objects.filter(country_from__exact=country_name).filter(~Q(**kwargs)).order_by('-' + order_variable, event_category + '_average_finish_place')
        stats_th11_activity_tag = 'stats_active_sort_button'



    # Code for making the points list with all the countries for each event.
    country_points_obj = CountriesInfo.objects.all()

    overall_country_points_list = []
    daily_country_points_list = []
    daily2_country_points_list = []
    weekly_country_points_list = []
    weekly2_country_points_list = []
    monthly_country_points_list = []

    for i in country_points_obj:
        overall_country_points_list.append(i.overall_points)
        daily_country_points_list.append(i.daily_points)
        daily2_country_points_list.append(i.daily2_points)
        weekly_country_points_list.append(i.weekly_points)
        weekly2_country_points_list.append(i.weekly2_points)
        monthly_country_points_list.append(i.monthly_points)

    overall_country_points_list.sort(reverse=True)
    daily_country_points_list.sort(reverse=True)
    daily2_country_points_list.sort(reverse=True)
    weekly_country_points_list.sort(reverse=True)
    weekly2_country_points_list.sort(reverse=True)
    monthly_country_points_list.sort(reverse=True)
    # Code for making the points list with all the countries for each event.



    country_qualified_drivers_obj = CountriesInfo.objects.filter(country_name__exact=country_name)

    overall_country_qualified_drivers = 0
    daily_country_qualified_drivers = 0
    daily2_country_qualified_drivers = 0
    weekly_country_qualified_drivers = 0
    weekly2_country_qualified_drivers = 0
    monthly_country_qualified_drivers = 0

    overall_country_points = 0
    daily_country_points = 0
    daily2_country_points = 0
    weekly_country_points = 0
    weekly2_country_points = 0
    monthly_country_points = 0

    for i in country_qualified_drivers_obj:
        overall_country_qualified_drivers = i.overall_number_of_drivers
        daily_country_qualified_drivers = i.daily_number_of_drivers
        daily2_country_qualified_drivers = i.daily2_number_of_drivers
        weekly_country_qualified_drivers = i.weekly_number_of_drivers
        weekly2_country_qualified_drivers = i.weekly2_number_of_drivers
        monthly_country_qualified_drivers = i.monthly_number_of_drivers

        overall_country_points = i.overall_points
        daily_country_points = i.daily_points
        daily2_country_points = i.daily2_points
        weekly_country_points = i.weekly_points
        weekly2_country_points = i.weekly2_points
        monthly_country_points = i.monthly_points

    if len(overall_country_points_list) != 0:
        overall_country_points_rank_in_the_world = overall_country_points_list.index(overall_country_points) + 1
        daily_country_points_rank_in_the_world = daily_country_points_list.index(daily_country_points) + 1
        daily2_country_points_rank_in_the_world = daily2_country_points_list.index(daily2_country_points) + 1
        weekly_country_points_rank_in_the_world = weekly_country_points_list.index(weekly_country_points) + 1
        weekly2_country_points_rank_in_the_world = weekly2_country_points_list.index(weekly2_country_points) + 1
        monthly_country_points_rank_in_the_world = monthly_country_points_list.index(monthly_country_points) + 1

    else:
        overall_country_points_rank_in_the_world = ''
        daily_country_points_rank_in_the_world = ''
        daily2_country_points_rank_in_the_world = ''
        weekly_country_points_rank_in_the_world = ''
        weekly2_country_points_rank_in_the_world = ''
        monthly_country_points_rank_in_the_world = ''



    context = {}

    context['object_ordered'] = object_ordered
    context['country_name'] = country_name
    context['event_category'] = event_category

    context['overall_country_points_rank_in_the_world'] = overall_country_points_rank_in_the_world
    context['daily_country_points_rank_in_the_world'] = daily_country_points_rank_in_the_world
    context['daily2_country_points_rank_in_the_world'] = daily2_country_points_rank_in_the_world
    context['weekly_country_points_rank_in_the_world'] = weekly_country_points_rank_in_the_world
    context['weekly2_country_points_rank_in_the_world'] = weekly2_country_points_rank_in_the_world
    context['monthly_country_points_rank_in_the_world'] = monthly_country_points_rank_in_the_world

    context['overall_country_qualified_drivers'] = overall_country_qualified_drivers
    context['daily_country_qualified_drivers'] = daily_country_qualified_drivers
    context['daily2_country_qualified_drivers'] = daily2_country_qualified_drivers
    context['weekly_country_qualified_drivers'] = weekly_country_qualified_drivers
    context['weekly2_country_qualified_drivers'] = weekly2_country_qualified_drivers
    context['monthly_country_qualified_drivers'] = monthly_country_qualified_drivers

    context['overall_stats_active_switch_button'] = overall_stats_active_switch_button
    context['daily_stats_active_switch_button'] = daily_stats_active_switch_button
    context['daily2_stats_active_switch_button'] = daily2_stats_active_switch_button
    context['weekly_stats_active_switch_button'] = weekly_stats_active_switch_button
    context['weekly2_stats_active_switch_button'] = weekly2_stats_active_switch_button
    context['monthly_stats_active_switch_button'] = monthly_stats_active_switch_button

    context['stats_th4_activity_tag'] = stats_th4_activity_tag
    context['stats_th5_activity_tag'] = stats_th5_activity_tag
    context['stats_th6_activity_tag'] = stats_th6_activity_tag
    context['stats_th7_activity_tag'] = stats_th7_activity_tag
    context['stats_th8_activity_tag'] = stats_th8_activity_tag
    context['stats_th9_activity_tag'] = stats_th9_activity_tag
    context['stats_th10_activity_tag'] = stats_th10_activity_tag
    context['stats_th11_activity_tag'] = stats_th11_activity_tag

    context['main_nav_button_1_tag'] = 'main_button_inactive'
    context['main_nav_button_2_tag'] = 'main_button_active'
    context['main_nav_button_3_tag'] = 'main_button_inactive'
    context['main_nav_button_4_tag'] = 'main_button_inactive'

    return render(request, 'country_stats.html', context)
"""------------------------------------------------COUNTRY STATS VIEW------------------------------------------------"""












"""------------------------------------------------ALL EVENTS VIEW------------------------------------------------"""
def all_events_view(request, event_category, date):

    obj_eventinfo = EventInfo.objects.filter(event_category__exact=event_category)

    obj_daily_eventinfo = EventInfo.objects.filter(event_category__exact='Daily')
    obj_daily2_eventinfo = EventInfo.objects.filter(event_category__exact='Daily2')
    obj_weekly_eventinfo = EventInfo.objects.filter(event_category__exact='Weekly')
    obj_Weekly2_eventinfo = EventInfo.objects.filter(event_category__exact='Weekly2')
    obj_Monthly_eventinfo = EventInfo.objects.filter(event_category__exact='Monthly')

    obj_leaderboard = LeaderBoard.objects.filter(event_info__event_category__exact=event_category, event_info__date__exact=date)


    daily_activity_class = ''
    daily2_activity_class = ''
    weekly_activity_class = ''
    weekly2_activity_class = ''
    monthly_activity_class = ''

    if event_category == 'Daily':
        daily_activity_class = 'event-options-container-active'

    elif event_category == 'Daily2':
        daily2_activity_class = 'event-options-container-active'

    elif event_category == 'Weekly':
        weekly_activity_class = 'event-options-container-active'

    elif event_category == 'Weekly2':
        weekly2_activity_class = 'event-options-container-active'

    elif event_category == 'Monthly':
        monthly_activity_class = 'event-options-container-active'


    date_selector_list = date_selector_cleaner(obj_eventinfo, 'EventInfo')

    date_selector_list_daily = date_selector_cleaner(obj_daily_eventinfo, 'EventInfo')
    date_selector_list_daily2 = date_selector_cleaner(obj_daily2_eventinfo, 'EventInfo')
    date_selector_list_weekly = date_selector_cleaner(obj_weekly_eventinfo, 'EventInfo')
    date_selector_list_weekly2 = date_selector_cleaner(obj_Weekly2_eventinfo, 'EventInfo')
    date_selector_list_monthly = date_selector_cleaner(obj_Monthly_eventinfo, 'EventInfo')


    position_list = []
    country_name_list = []
    name_list = []
    vehicle_list = []
    time_list = []
    time_seconds_list = []
    diff_1st_list = []
    player_id_list = []
    earned_points_list = []

    for i in obj_leaderboard:

        position_list.append(i.position)
        country_name_list.append(i.country_name)
        name_list.append(i.name)
        vehicle_list.append(i.vehicle)
        time_list.append(i.time)
        time_seconds_list.append(i.time_seconds)
        diff_1st_list.append(i.diff_1st)
        player_id_list.append(i.player_id)
        earned_points_list.append(i.earned_points)


    # START of reverse list script.
    reverse_list = position_list[::-1]
    position_list = reverse_list

    reverse_list = country_name_list[::-1]
    country_name_list = reverse_list

    reverse_list = name_list[::-1]
    name_list = reverse_list

    reverse_list = vehicle_list[::-1]
    vehicle_list = reverse_list

    reverse_list = time_list[::-1]
    time_list = reverse_list

    reverse_list = diff_1st_list[::-1]
    diff_1st_list = reverse_list

    reverse_list = player_id_list[::-1]
    player_id_list = reverse_list

    reverse_list = earned_points_list[::-1]
    earned_points_list = reverse_list
    # END of reverse list script.


    zipped_leader_list = list(zip(position_list, country_name_list, name_list,
                                  player_id_list, vehicle_list,time_list, diff_1st_list, earned_points_list
                                  ))

    date = ''
    event_name = ''
    location = ''
    stage = ''
    time_of_the_day = ''
    weather = ''
    total_drivers = 0

    for info in obj_leaderboard:

        date = info.event_info.date
        event_name = info.event_info.event_name
        location = info.event_info.location
        stage = info.event_info.stage
        time_of_the_day = info.event_info.time_of_the_day
        weather = info.event_info.weather
        total_drivers = info.event_info.total_drivers
        break


    context = {}

    context['daily_options_container_active'] = daily_activity_class
    context['daily2_options_container_active'] = daily2_activity_class
    context['weekly_options_container_active'] = weekly_activity_class
    context['weekly2_options_container_active'] = weekly2_activity_class
    context['monthly_options_container_active'] = monthly_activity_class

    context['event_category'] = event_category

    context['date_selector_list'] = date_selector_list
    context['last_daily_date'] = date_selector_list_daily[0]
    context['last_daily2_date'] = date_selector_list_daily2[0]
    context['last_weekly_date'] = date_selector_list_weekly[0]
    context['last_weekly2_date'] = date_selector_list_weekly2[0]
    context['last_monthly_date'] = date_selector_list_monthly[0]
    context['date'] = date
    context['event_name'] = event_name
    context['location'] = location
    context['stage'] = stage
    context['time_of_the_day'] = time_of_the_day
    context['weather'] = weather
    context['total_drivers'] = total_drivers
    context['zipped_leader_list'] = zipped_leader_list
    context['total_unique_drivers'] = total_unique_drivers()
    context['most_participants_ever_value'] = most_participants_ever()[0]
    context['most_participants_ever_event'] = most_participants_ever()[1]
    context['most_participants_ever_date'] = most_participants_ever()[2]

    context['main_nav_button_1_tag'] = 'main_button_inactive'
    context['main_nav_button_2_tag'] = 'main_button_inactive'
    context['main_nav_button_3_tag'] = 'main_button_active'
    context['main_nav_button_4_tag'] = 'main_button_inactive'

    return render(request, 'all_events.html', context)
"""------------------------------------------------ALL EVENTS VIEW------------------------------------------------"""











"""------------------------------------------------HOW THIS SITE WORKS VIEW------------------------------------------------"""
def how_this_site_works_view(request):

    context = {}

    context['main_nav_button_1_tag'] = 'main_button_inactive'
    context['main_nav_button_2_tag'] = 'main_button_inactive'
    context['main_nav_button_3_tag'] = 'main_button_inactive'
    context['main_nav_button_4_tag'] = 'main_button_active'

    return render(request, 'how_this_site_works.html', context)
"""------------------------------------------------HOW THIS SITE WORKS VIEW------------------------------------------------"""






