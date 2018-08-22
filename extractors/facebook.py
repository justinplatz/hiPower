import urllib
import json
import requests

def get_data_from_feed(access_token):
    url = "https://graph.facebook.com/v3.1/me/feed?fields=message%2Cstory%2Ccreated_time%2Cid%2Cpicture%2Cplace%2Cname%2Clink%2Cevent%2Capplication%2Ccaption%2Cprivacy%2Cupdated_time%2Cbackdated_time%2Ccoordinates%2Ctimeline_visibility%2Cshares%2Cadmin_creator%2Cactions%2Cfeed_targeting%2Ctype%2Ctargeting%2Cvia%2Cis_popular%2Cproperties%2Csource%2Cdescription%2Cfull_picture%2Cfrom%2Cwith_tags%2Cmessage_tags%2Cis_published%2Cis_instagram_eligible%2Cis_live_audio%2Cis_spherical%2Cis_hidden%2Cis_expired%2Cis_crossposting_eligible%2Cstory_tags%2Ctarget%2Cwidth%2Cheight%2Cpermalink_url%2Cobject_id%2Cstatus_type%2Cicon%2Cparent_id%2Csubscribed%2Ccall_to_action%2Cchild_attachments%2Ccomments_mirroring_domain%2Cexpanded_height%2Cexpanded_width%2Cinstagram_eligibility%2Cinstream_eligibility%2Cpromotion_status%2Cscheduled_publish_time&access_token=" + access_token

    r = requests.get(url = url)
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        return "error getting data from feed"

def get_data_from_user(access_token):
    url = "https://graph.facebook.com/v3.1/me?fields=about%2Caddress%2Cage_range%2Cbirthday%2Ccan_review_measurement_request%2Ccontext%2Ceducation%2Cemail%2Cfavorite_athletes%2Cfavorite_teams%2Cfirst_name%2Cgender%2Chometown%2Cid%2Cinspirational_people%2Cinstall_type%2Cinstalled%2Cinterested_in%2Cis_famedeeplinkinguser%2Cis_shared_login%2Clanguages%2Clast_name%2Clink%2Cmeeting_for%2Clocation%2Cmiddle_name%2Cname%2Cname_format%2Cpayment_pricepoints%2Cpolitical%2Cpublic_key%2Cquotes%2Crelationship_status%2Creligion%2Csecurity_settings%2Cshared_login_upgrade_required_by%2Cshort_name%2Csignificant_other%2Csports%2Ctest_group%2Cvideo_upload_limits%2Cviewer_can_send_gift%2Cwebsite%2Cwork&access_token=" + access_token

    r = requests.get(url = url)
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        return "error getting data from profile"

def main():

    access_token = "EAAGcZAUhKVZAwBAJDylzbVkAc2BFMXIVsqvGmV0YuuLKRDWAZAc013lW2U4Tu2BOY9YslZAyR6ttLSgtedSh0tVLWvoYQY2iR1HA63SLZBpYYn6PIJCJA2qBc9YlcSAuplZBGxvKGRMjnXUQNl8mYSqqvVDo7lAe9c5y9VxZB77djsLhzUVcsCUThkMpSZAEdaYZD"

    print(get_data_from_feed(access_token))
    print(get_data_from_user(access_token))


main()
