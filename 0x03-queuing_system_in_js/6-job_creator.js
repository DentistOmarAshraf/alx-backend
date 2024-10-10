import kue from 'kue';

const obj = {
    phoneNumber: "01017815609",
    message: "Hello My name is Omar"
}

const push_notification_code = kue.createQueue();

const job = push_notification_code.create('message', obj)
    .save(err => {
        if (!err) console.log(`Notification job created: ${job.id}`);
    });

push_notification_code.process('message', 1, (job, done) => {
    console.log(`Notification job completed`);
})

push_notification_code.on('job failed', (id, error) => {
    console.log('Notification job failed');
})