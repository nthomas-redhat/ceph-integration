from tendrl.ceph_integration import objects
from tendrl.ceph_integration.flows import CephIntegrationBaseFlow
from tendrl.ceph_integration.objects.rbd import Rbd
from tendrl.commons.event import Event
from tendrl.commons.message import Message


class DeleteRbd(CephIntegrationBaseFlow):
    obj = Rbd
    def __init__(self, *args, **kwargs):
        super(DeleteRbd, self).__init__(*args, **kwargs)

    def run(self):
        Event(
            Message(
                priority="info",
                publisher=tendrl_ns.publisher_id,
                payload={
                    "message": "Starting deletion flow for rbd %s" %
                    (self.parameters['Rbd.name'])
                    },
                request_id=self.request_id,
                flow_id=self.uuid,
                cluster_id=tendrl_ns.tendrl_context.integration_id,
            )
        )

        super(DeleteRbd, self).run()