const util = require('../utils/util');
const auth = require('../utils/auth');

function verify(requestBody) {
    if(!requestBody.user || !requestBody.usermail || !requestBody.token) {
        return util.buildResponse(401, {
            verified: false,
            message: "Incorrect request body"
        })
    }

    const user = requestBody.user;
    const token = requestBody.token;
    const verification = auth.verifyToken(user.usermail, token);

    if(!verification.verified) {
        return util.buildResponse(401, verificattion);
    }

    return util.buildResponse(200, {
        verified: true,
        message: 'success',
        user: user,
        token: token

    })
}

module.exports.verify = verify;
