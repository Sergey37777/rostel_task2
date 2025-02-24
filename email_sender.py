from typing import List

from config.constants.variables import SMTP_SERVER, SMTP_PORT, SMTP_LOGIN, SMTP_PASSWORD, RECIPIENT_EMAIL
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from config.logger import logger



class EmailSender:
    @staticmethod
    def send_text_email(subject: str, body: str, to_emails: List[str], from_email: str) -> None:
        try:
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = ', '.join(to_emails)
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
        except Exception as e:
            logger.warning('Ошибка при формировании письма')

        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(SMTP_LOGIN, SMTP_PASSWORD)
            server.sendmail(msg['From'], to_emails, msg.as_string())
            server.quit()
            logger.info('Письмо успешно отправлено')
        except Exception as e:
            logger.warning(f'Ошибка при отправке письма: {e}')