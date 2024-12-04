import kue from 'kue';

const queue = kue.createQueue();

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    const total = 100;
    function next(i) {
      if (i === 0 || i === (total / 2)) {
        job.progress(i, total);
        if (i === (total / 2)) { console.log(`Sending notification to ${phoneNumber}, with message: ${message}`); }
      }
      if (blacklistedNumbers.includes(job.data.phoneNumber)) {
        return done(new Error(`Phone number ${job.data.phoneNumber} is blacklisted`));
      }
      if (i === total) { return done(); }
      return next(i + 1);
    }
    next(0);
  }

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

