from cas_client import CASClient
from .faculty_info import KD_ORG


def get_sso_profile(raw_sso_data):
  try:
    sso_profile = {
      "username": raw_sso_data['user'],
      "attributes": {**raw_sso_data["attributes"], 'kd_org': KD_ORG[raw_sso_data["attributes"]['kd_org']]}
    }
    return sso_profile, False
  except Exception as e:
    return None, False

def authenticate(ticket, service_url, cas_url="https://sso.ui.ac.id/cas2"):
  cas = CASClient(cas_url, auth_prefix='')
  if ticket is not None and service_url is not None:
    try:
      cas_response = cas.perform_service_validate(
        ticket=ticket,
        service_url=service_url
      )

      if cas_response and cas_response.success:
        sso_profile, is_error = get_sso_profile(cas_response.data)

        if is_error:
          return True, None

        return False, sso_profile

      return False, None

    except Exception as e:
      print(e)
      return True, None
  return False, None


def get_login_url(service_url, cas_url="https://sso.ui.ac.id/cas2"):
  cas = CASClient(cas_url, auth_prefix='')
  return cas.get_login_url(service_url=service_url)

def get_logout_url(service_url, cas_url="https://sso.ui.ac.id/cas2"):
  cas = CASClient(cas_url, auth_prefix='')
  return cas.get_logout_url(service_url=service_url)





  
  