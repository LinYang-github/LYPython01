import sys

# argv �����в����������ű�����
# exit([arg]) �˳���ǰ�ĳ��򣬿�ѡ����Ϊ�����ķ���ֵ���ߴ�����Ϣ
# modules ӳ��ģ�����Ƶ�����ģ����ֵ�
# path ����ģ������Ŀ¼��Ŀ¼���б�
# platform ����sunos5����win32��ƽ̨��ʶ��
# stdin ��׼������-һ�����ļ���file-like������
# stdout ��׼�����-һ�����ļ�����
# stderr ��׼������-һ�����ļ�����

args = sys.argv[1:]
args.reverse()
print ' '.join(args)
