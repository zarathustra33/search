hunterEmails={}
hunterEmails['kirby']='kirby.deng@ocbang.com'
# hunterEmails['kirby']='sharon.xu@ocbang.com'
hunterEmails['lewis']='lewis.guo@ocbang.com'
# hunterEmails['ella']='ella.zhao@ocbang.com'
hunterEmails['ella']='ella.zhao@ocbang.com'
# hunterEmails['fiona']='fiona.mao@ocbang.com'
hunterEmails['fiona']='fiona.mao@ocbang.com'
# hunterEmails['lewis']='lewis.guo@ocbang.com'
# hunterEmails['jack']='jack.zhu@ocbang.com'
hunterEmails['jack']='jack.zhu@ocbang.com'
hunterEmails['nina']='nina.li@ocbang.com'
# hunterEmails['nina']='sharon.xu@ocbang.com'

# hunterEmails['helena']='helena.li@ocbang.com'
# hunterEmails['helena']='sharon.xu@ocbang.com'
hunterEmails['audrey']='audrey.liu@ocbang.com'
# hunterEmails['audrey']='sharon.xu@ocbang.com'
hunterEmails['amy']='amy.wang@ocbang.com'
hunterEmails['allison']='allison.ma@ocbang.com'
hunterEmails['sharon']='sharon.xu@ocbang.com'

def group_candidates(luckyRecruiter,test_profiles,hunterEmails):
    grouped_candidates={}
    for recruiter in luckyRecruiter:
        if recruiter!=None:
            if recruiter in hunterEmails.keys():
                grouped_candidates[recruiter]=[p for p in test_profiles if p['hunter']==recruiter]
            else:
                grouped_candidates['kirby']=[p for p in test_profiles if p['hunter']==recruiter]
        else:
    ## if hunter is none, then send to kirby's email
            if grouped_candidates.get('hunter')==None:
                grouped_candidates['kirby']=[p for p in test_profiles if p['hunter']==None]
    # print('hello')
    return grouped_candidates

def generate_body_html(grouped_candidates, position,hunter):
    numCandidates=len(grouped_candidates)
    numCandidates=len(grouped_candidates)
    ol_html=str()
    for candidate in grouped_candidates:
        this_list_html='<li> <a href={url}> <b> {name}</b> </a> : Current {position} at <b> {company} </b> <br> with totally <b>{years} </b>years of work experience  </li>'.format(url=candidate['bytedance_application_link'],name=candidate['name'],position=candidate['experience'][0]['Position'],company=candidate['experience'][0]['Company'],years=candidate['work_experience'])
        ol_html+=this_list_html
    BODY_HTML = """<html>
<head></head>
<body>
  <h3>You have candidates macthed up with the new position for {new_position}</h1>
  <p> Hi {name}! There are totally <b> {count_candidate} </b> candidates that could be a good match! </p> <br>
    <ol>
   {ol_html}
   </ol>
  <p> You can browse the candidate's profile in Bytedance's hunter system by clicking the candidate's name </p>
  <br>
  <p> How is the result? If the recommended candidate doesn't fit the position, please help us improve the database by filling the survey below. It's pretty short! just 3 quick questions <a href="https://forms.gle/H91avRT3GZ8nczUr9"> disqualified candidate feedback</a> </p>
  
  <br>
  <br>
  <p> Sharon Xu </p>
</body>
</html>
            """  .format(count_candidate=numCandidates,ol_html=ol_html,new_position=position,name=hunter)
    # print(BODY_HTML)
    return(BODY_HTML)


def send_email_to_lucky_hunter(matched_candidates,position):
    import boto3
    from botocore.exceptions import ClientError
    AWS_REGION = "us-west-2"
    SENDER = "sharon xu <sharon.xu@ocbang.com>"
    hunters=matched_candidates.keys()
    CONFIGURATION_SET = "ConfigSet"
    AWS_REGION = "us-west-2"
    CHARSET = "UTF-8"
    BODY_TEXT = ("Amazon SES Test (Python)\r\n"
             "This email was sent with Amazon SES using the "
             "AWS SDK for Python (Boto)."
            )
    client = boto3.client('ses',region_name=AWS_REGION)
    SUBJECT='OCBang: you have candidates matched with ' + position
    for lucky_hunter in hunters:
        grouped_candidates=matched_candidates[lucky_hunter]
        RECIPIENT=hunterEmails[lucky_hunter]
        BODY_HTML=generate_body_html(grouped_candidates,position,lucky_hunter)
        try:
            #Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,
                # If you are not using a configuration set, comment or delete the
                # following line
        #         ConfigurationSetName=CONFIGURATION_SET,
            )
        # Display an error if something goes wrong.	
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(lucky_hunter)
            print(response['MessageId'])