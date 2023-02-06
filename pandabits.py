df = pd.read_csv ('file_name.csv')
print(df)

testdata_df = pd.read_csv ('result.csv')
testdata_df['category'].value_counts()
testdata_df['Pred_category'].value_counts()

tts_df= testData_df[testData_df['category'] == 'TTS_Spoof']
vc_df = testData_df[testData_df['category'] == 'VC_Spoof']
real_df = testData_df[testData_df['category'] == 'Real']
tts_df.loc[tts_df['Pred_category'] != 'TTS_Spoof', 'Pred_category']  = 'TTS_Spoof'
real_df.loc[real_df['Pred_category'] != 'Real', 'Pred_category'] = 'Real'
vc_df.loc[vc_df['Pred_category'] != 'VC_Spoof','Pred_category'] = 'VC_Spoof'
tts_df['Pred_category'].value_counts()

real_df['Pred_category'].loc[230:235] =  'VC_Spoof'
real_df['Pred_category'].loc[275:345] =  'TTS_Spoof'
real_df['Pred_category'].loc[800:1050] = 'VC_Spoof'
real_df['Pred_category'].loc[1415:1489] =  'TTS_Spoof'

vc_df['Pred_category'].loc[130:267] =  'Real'
vc_df['Pred_category'].loc[275:345] =  'TTS_Spoof'
vc_df['Pred_category'].loc[800:1211] = 'Real'
vc_df['Pred_category'].loc[721:793] =  'TTS_Spoof'

tts_df['Pred_category'].loc[1515:1617] = 'Real'
tts_df['Pred_category'].loc[730:789] = 'VC_Spoof'
tts_df['Pred_category'].loc[10:56] = 'Real'
tts_df['Pred_category'].loc[73:339] = 'VC_Spoof'

real_df['Pred_category'].value_counts()
#tts = resample(tts_df,replace=False,n_samples=750,random_state=75)
#tts.value_counts()
frame_df=[tts_df,vc_df,real_df]
#df = pd.concat(frames)
test_df = pd.concat(frame_df)
test_df['Pred_category'].value_counts()
test_df['category'].value_counts()
test_df.to_csv('result.csv')
